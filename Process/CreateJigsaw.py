"""
Simple script to segment an image into jigsaw pieces. Steps are as follows:
1. Segment image using superpixels method
2. Manipulate boundaries to create interlocking pieces
3. Remove intersections and impose boundary conditions

Acknowledgements:
Superpixel code from: https://www.pyimagesearch.com/2014/07/28/a-slic-superpixel-tutorial-using-python/
"""

# import the necessary packages
from skimage.segmentation import slic
from skimage.segmentation import mark_boundaries
from skimage.util import img_as_float
from skimage import io
import matplotlib.pyplot as plt
import argparse

def _parse_args():
    """construct the argument parser and parse the arguments"""
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required = True, help = "Path to the image")
    ap.add_argument("-s", "--segments", required = True, help = "Number of segments")
    ap.parse_args()
    
    return ap

def _segment_image(image, num_segments):
    # load the image and convert it to a floating point data type
    image = img_as_float(io.imread(args["image"]))
 
    # apply SLIC and extract (approximately) the supplied number
    # of segments
    segments = slic(image, n_segments = numSegments, sigma = 5)
 
    # show the output of SLIC
    fig = plt.figure("Superpixels -- %d segments" % (numSegments))
    ax = fig.add_subplot(1, 1, 1)
    ax.imshow(mark_boundaries(image, segments))
    plt.axis("off")
 
    # show the plots
    plt.show()

if __name__ == '__main__':
    ap = _parse_args()
    _segment_image(ap.image, ap.segments)
