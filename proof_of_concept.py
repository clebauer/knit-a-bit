# -*- coding: utf-8 -*-
# <nbformat>4</nbformat>

# <codecell> {"scrolled": true}

def knitting_pattern(mapping, sample_data, width):
    total = 0
    total2 = 0
    pattern = 'CAST ON {} STS\n\n'.format(width)
    
    for i in range(0, len(sample_data)):
        stitch = mapping[sample_data[i]]
        if (total + stitch['needed'] > width):
            for j in range(0, width - total):
                total += 1
                pattern += '{} (Total: {})\n'.format('K', total)
            total = 0 
            total2 = 0
            pattern += '\nNEW ROW\n\n'
        total += stitch['needed'] 
        total2 += stitch['created']
            
        pattern +='{} (Total: {} now, {} left)\n'.format(stitch['abbrev'],
                                                     total2,
                                                     width-total)
    for j in range(0, width - total):
            total += 1
            pattern +='{} (Total: {})\n'.format('K', total)
    
    pattern +='\nCAST OFF {} sts'.format(width)
    return pattern

# <codecell> {"collapsed": true}

mapping = {0:{'abbrev':'K',     'needed':1, 'created':1,},
           1:{'abbrev':'P',     'needed':1, 'created':1,},
           2:{'abbrev':'YO',    'needed':0, 'created':1,},
           3:{'abbrev':'K2TOG', 'needed':2, 'created':1}}

sample_data = [3, 2, 3, 2, 3, 2, 3, 2, 2, 3, 
               0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
               1, 1, 1, 1, 1, 1, 1, 1, 1, 
               3, 2, 3, 2, 2, 0, 2]

width = 10

# if a row asks for more stitches than it has available, it will move that
# stitch request to the next row and pad the row with knit stitches.

# <codecell> {}

print knitting_pattern(mapping, sample_data, width)

# <codecell> {"collapsed": true}



# <metadatacell>

{"kernelspec": {"display_name": "Python 2", "name": "python2", "language": "python"}}