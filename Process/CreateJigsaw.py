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
from skimage.segmentation import mark_boundaries, find_boundaries
from skimage.util import img_as_float
from skimage import io
import matplotlib.pyplot as plt
import argparse

def _parse_args():
    """construct the argument parser and parse the arguments"""
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required = True, help = "Path to the image")
    ap.add_argument("-s", "--segments", required = True, type=int, help = "Number of segments")
    
    return ap.parse_args()

def _segment_image(image_path, num_segments):
    # load the image and convert it to a floating point data type
    image = img_as_float(io.imread(image_path))
 
    # apply SLIC and extract (approximately) the supplied number
    # of segments
    segments = slic(image, 
                    n_segments=num_segments,
                    sigma=5,
                    compactness=30,
                    enforce_connectivity=True,
                    slic_zero=True)

    boundaries = find_boundaries(segments)
    # show the output of SLIC
    fig = plt.figure("Superpixels")
    ax = fig.add_subplot(1, 1, 1)
    ax.imshow(find_boundaries(segments))
    plt.axis("off")
  
    # show the plots
    plt.show()

if __name__ == '__main__':
    ap = _parse_args()
    _segment_image(ap.image, ap.segments)
