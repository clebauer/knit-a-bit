from flask import Flask
import struct
from PIL import Image
from IPython.display import Image as iImage
import numpy as np
import scipy
import scipy.misc
import scipy.cluster
import binascii
import io

app = Flask(__name__)

@app.route('/')
def color(name=None):
    NUM_CLUSTERS = 10
    im = Image.open('test.jpg')
    im = im.resize((150, 150))      # optional, to reduce time
    ar = np.asarray(im)
    shape = ar.shape
    ar = ar.reshape(np.product(shape[:2]), shape[2]).astype(float)

    codes, dist = scipy.cluster.vq.kmeans(ar, NUM_CLUSTERS)

    vecs, dist = scipy.cluster.vq.vq(ar, codes)         # assign codes
    counts, bins = np.histogram(vecs, len(codes))    # count occurrences

    index_max = np.argmax(counts)                    # find most frequent
    peak = codes[index_max]
    colour = binascii.hexlify(str.encode(''.join(chr(int(c)) for c in peak)))
    
    test_img = Image.new('RGB', (300, 200),tuple([int(x) for x in peak]))
    return render_template('home.html', name=name)
