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
import numpy as np
from scipy.spatial import Voronoi, voronoi_plot_2d

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

    return segments,boundaries

def plot_puzzle(segments):
    # show the output of SLIC
    fig = plt.figure("Superpixels")
    ax = fig.add_subplot(1, 1, 1)
    ax.imshow(find_boundaries(segments))
    plt.axis("off")
  
    # show the plots
    plt.show()

def determine_medoids(segments):
    """
    each medoid is the closest real datapoint to the centroid. 
    The centroid's component is the average of values in that dimension for all membership elements
    """

    resultant_medoids=list()

    # for each cluster
    for i in range(segments.min(),segments.max()):
        
        #get a list of array positions for the current cluster
        indices=np.argwhere(segments==i)
        #take the average of those cluster positions in the 0th and 1th dimension
        #round them to be real pixels
        centroid_component_0=np.round(np.mean(indices[:,0]),0)
        centroid_component_1=np.round(np.mean(indices[:,1]),0)

        resultant_medoids.append(
            [centroid_component_0,centroid_component_1]
        )

    return np.array(resultant_medoids)
    
def merge_clusters():
    """
    clusters might be too close too one another, concentric, or oddly shaped
    one heuristic that could catch this is if the medoids are within some tolerance
    of one another
    """
    pass

def create_Voronoi_object(medoids):

    my_Voronoi=Voronoi(medoids)
    voronoi_plot_2d(my_Voronoi)
    plt.show()


if __name__ == '__main__':
    ap = _parse_args()
    segments,_=_segment_image(ap.image, ap.segments)
    print(segments)
    medoids=determine_medoids(segments)
    # print(medoids)
    plot_puzzle(segments)
    create_Voronoi_object(medoids)