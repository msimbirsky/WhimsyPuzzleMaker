from skimage.segmentation import slic, mark_boundaries, find_boundaries
from skimage.data import astronaut
from matplotlib import pyplot as plt
from skimage.measure import regionprops, find_contours
import numpy as np
import pandas as pd
import csv

#import stock/test image
img = astronaut()

#segment the image
segments = slic(img, n_segments=250, compactness=50, sigma=0.5)

#display segmented image
plt.imshow(mark_boundaries(img, segments))
plt.show()

#save numerical representation of segmented image
np.savetxt("segments.txt", segments, fmt='%i')

#get coordinates and labels of segments
regions = regionprops(segments)
for props in regions:
    print(f'the label is {props.label}')
    print(f'the coordinates are {props.coords}')

#write coordinates of segment contours to csv   
contours = find_contours(segments)
with open("contours.csv", "w", encoding='utf8') as csvfile:
    hrd = csv.writer(csvfile)
    hrd.writerow(["C%d"%d for d in range(1,1+len(contours))])
    for r in zip(*contours):
        hrd.writerow(r)  

#generate csv with each cell representing a pixel and denoting in a boolean manner whether the pixel is a boundary or not
boundaries = find_boundaries(segments)
with open("boundaries.csv", "w", encoding='utf8') as csvfile:
    hrd = csv.writer(csvfile)
    hrd.writerow(["C%d"%d for d in range(1,1+len(boundaries))])
    for r in zip(*boundaries):
        hrd.writerow(r)  