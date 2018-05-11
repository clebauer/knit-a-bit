# -*- coding: utf-8 -*-
# <nbformat>4</nbformat>

# <codecell> {"scrolled": true}

# PROOF OF CONCEPT

import random

# define width of pattern
width = 10

# generates temporary number of data points i'm pulling
total_data_pts = random.randint(40,50)


sample_data = []
# for each pretend data point
for x in range(0, total_data_pts):
    # generate a random number to be considered the "actual data point gathered"
    num = random.randint(0,3)
    sample_data.append(num)
    


mapping = {0:{'stitch':'K',     'st_use':1, 'st_now':1,},
           1:{'stitch':'P',     'st_use':1, 'st_now':1,},
           2:{'stitch':'YO',    'st_use':0, 'st_now':1,},
           3:{'stitch':'K2TOG', 'st_use':2, 'st_now':1}}

knitting_pattern = 'CAST ON {} STS\n'.format(width)

prev_row_ct = width
curr_row_ct = 0

# for each stitch (ex: 3)
# map to appropriate stitch (ex: K2TOG, st_use: 2)
# check if the prev_row_ct is greater than 0.
# if it is, then:
    # subtract st_use value from prev_row_ct to set how many stitches we have left to use
    # add st_now value to curr_row_ct to set how many stitches we currently have.
# if it isn't:
    # it's either 0 or it's -1
    # if it's -1

for x in sample_data:
    

    max_st -= (1- mapping[x]['st_gain'])
    if max_st <= 0:
        max_st += width
        knitting_pattern += '({} st)\n'.format(max_st)
    knitting_pattern += (mapping[x]['stitch'] + ' ')
    



print knitting_pattern

# <codecell> {"collapsed": true}



# <metadatacell>

{"kernelspec": {"display_name": "Python 2", "name": "python2", "language": "python"}}