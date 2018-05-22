# -*- coding: utf-8 -*-
# <nbformat>4</nbformat>

# <markdowncell> {}

# Some edge-cases to consider:
# 1. When the last stitch needs more stitches than the row contains.
# 2. When the first or last stitch is a yarn-over (https://giphy.com/explore/nope-dont-like-that)
# 3. Crochet stitch mapping looks w e i r d.
# 
# And things to implement:
# 1. Amount of yarn estimator (both vague and with input).
# 2. Color suggestions
# 3. Later on, make for crochet!


# <codecell> {"collapsed": true}

def gen_mapping(craft='knitting'):
    mapping = {}
    if craft == 'knitting':
        mapping = {0:{'name':'k',     'needed':1,  'created':1,},
                   1:{'name':'p',     'needed':1,  'created':1,},
                   2:{'name':'yo',    'needed':0,  'created':1,},
                   3:{'name':'k2tog', 'needed':2,  'created':1}}
    else:#if craft == 'crochet':
        mapping = {0:{'name':'sc',     'needed':1, 'created':1},
                   1:{'name':'dc',     'needed':1, 'created':1},
                   2:{'name':'ch',     'needed':0, 'created':0},
                   3:{'name':'sc2tog', 'needed':2, 'created':1}}
    return mapping

# <codecell> {"collapsed": true}

def cast_on(num_sts):
    return 'Cast on {} sts\n\n'.format(num_sts)

def cast_off(num_sts):
    return '\nCast off {} sts'.format(num_sts)

def row_def(row_num):
    return ['Row #{}: '.format(row_num)]

def physically_write_pattern(starting_width, ending_width, instructions):
    text_pattern = ''
    text_pattern += cast_on(starting_width)
    for x in range(0, len(instructions), 3):
        text_pattern += '{} {} ({} sts)\n'.format(instructions[x][0],
                                                  ' '.join(instructions[x+1]),
                                                  instructions[x+2][0])
    
    text_pattern += cast_off(ending_width)
    return text_pattern

# <codecell> {"scrolled": true, "collapsed": true}

def pattern_generator(sample_data, starting_width, mapping='default'):
    # pull the 0-3 mapping for new projects, given the right craft.
    mapping = gen_mapping('knitting')
    
    # with the mapping in hand, set up our counters
    row_counter = 1
    
    # determine the previous row width (stitch count) and current row width counters
    prev_row_width = starting_width
    curr_row_width = 0
    ending_width = 0
    
    # create a placeholder to place all instruction rows into
    instructions = [row_def(row_counter)]
    line = []
        
    # while there are still stitches to implement,
    while(sample_data):
        # grab that stitch, remove it from the available stitches, and map it to its stitch
        elem = sample_data.pop(0)
        st = mapping[elem]
        
        # if we still have stitches to work with
        if prev_row_width >= st['needed']:
            prev_row_width -= st['needed']  # keep track of old stitches being used.
            curr_row_width += st['created'] # keep track of new stitches being created.
            line.append(st['name'])         # add the new stitch to the line of instruction
        # otherwise, we want to push the instructions to be stored and reset
        else:
            #line += ['k' for x in range(0, prev_row_width)] # if st left less than next st, pad row with 'k' stitches
            instructions.append(line)                       # place the line into the instructions
            line = [st['name']]                             # reset the line
            prev_row_width = curr_row_width - st['needed']  # reset the prev_row_width
            curr_row_width = st['created']                  # reset the curr_row_width
            row_counter += 1                                # increment row counter
            instructions.append([str(prev_row_width + st['needed'])])
            instructions.append(row_def(row_counter))       # place the new row counter into the instructions
    else:
        line += ['k' for x in range(0, prev_row_width)] # if st left less than next st, pad row with 'k' stitches
        ending_width = curr_row_width + prev_row_width
        instructions.append(line) # place the last line into the instructions 
        
        instructions.append([ending_width])

    #return instructions
    return physically_write_pattern(starting_width, ending_width, instructions)  

# <codecell> {}

sample_data = [3, 2, 3, 2, 3, 2, 3, 2, 2, 3, 
               0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
               1, 1, 1, 1, 1, 1, 1, 1, 1, 
               3, 2, 3, 2, 2, 0, 2]

print pattern_generator(sample_data, 10)

# <codecell> {"collapsed": true}

# Now it's time to test my program for a section of randomly generated data

# <codecell> {"scrolled": true}

import random
data_point_length = random.randint(40,60)

data_points = []

for i in range(data_point_length):
    data_points.append(random.randint(0,3))

print data_points, '\n'

print pattern_generator(data_points, 10)

# <metadatacell>

{"kernelspec": {"display_name": "Python 2", "name": "python2", "language": "python"}}