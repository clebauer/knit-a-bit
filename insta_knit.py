# -*- coding: utf-8 -*-
# <nbformat>4</nbformat>

# <codecell> {"collapsed": true}

# https://stackoverflow.com/questions/3241929/python-find-dominant-most-common-color-in-an-image


# <codecell> {}

import struct
from PIL import Image
import numpy as np
import scipy
import scipy.misc
import scipy.cluster

NUM_CLUSTERS = 10

print 'reading image'
im = Image.open('shoes.jpg')
im = im.resize((150, 150))      # optional, to reduce time
ar = np.asarray(im)
shape = ar.shape
ar = ar.reshape(scipy.product(shape[:2]), shape[2]).astype(float)

print 'finding clusters'
codes, dist = scipy.cluster.vq.kmeans(ar, NUM_CLUSTERS)
print 'cluster centres:\n', codes

vecs, dist = scipy.cluster.vq.vq(ar, codes)         # assign codes
counts, bins = scipy.histogram(vecs, len(codes))    # count occurrences

index_max = scipy.argmax(counts)                    # find most frequent
peak = codes[index_max]
colour = ''.join(chr(int(c)) for c in peak).encode('hex')

# <codecell> {"collapsed": true}

colors = {}
sorted_order = np.argsort(counts)[::-1]
for i in range(len(sorted_order)):
    elem_num = sorted_order[i]
    peak = codes[elem_num]
    colour = ''.join(chr(int(c)) for c in peak).encode('hex')
    colors[i] = {colour:counts[elem_num]}

# <codecell> {}

colors

# <codecell> {"collapsed": true}



# <metadatacell>

{"kernelspec": {"display_name": "Python 2", "name": "python2", "language": "python"}}