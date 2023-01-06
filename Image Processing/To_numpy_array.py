import os
from PIL import Image
import numpy as np
from image_processing import im

from numpy import asarray
dirpath='/Users/kimjuhwan/Desktop/Nonpuddle-gray2/'
nonpuddle_img_list = os.listdir(dirpath)
nonpuddle_to_numpy=[]


for i in nonpuddle_img_list:
    if not i.endswith('.jpeg'):
        nonpuddle_img_list.remove(i)
#print(nonpuddle_img_list)
print(len(nonpuddle_img_list))

for i in nonpuddle_img_list:
    img=Image.open(dirpath+i)
    numpydata = asarray(img)
    nonpuddle_to_numpy.append(numpydata)

np.save('/Users/kimjuhwan/Desktop/npderivatives/npg2.npy',nonpuddle_to_numpy)
