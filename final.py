import os
import cv2
from PIL import Image
import numpy as np
from numpy import asarray
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.ensemble import ExtraTreesClassifier
#from ExTC import ET

#-------------------------------------------------------

dirpath="/Users/kimjuhwan/Desktop/testfolder/puddle.png"
to_numpy=[]

img=Image.open(dirpath).convert('L')
resized=img.resize((256,256))

numpydata = asarray(resized)
to_numpy.append(numpydata)

np.save('/Users/kimjuhwan/Desktop/testfolder/puddle.npy', to_numpy)

p_dir = '/Users/kimjuhwan/Desktop/npderivatives/pg2.npy'
np_dir = '/Users/kimjuhwan/Desktop/npderivatives/npg2.npy'
test_dir = '/Users/kimjuhwan/Desktop/testfolder/puddle.npy'

Answer = ET(p_dir,np_dir,test_dir)

if Answer == 1:
    img = cv2.imread(dirpath)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #img = cv2.imdecode(imgnp,0)

    #img = cv2.imdecode(im,0)
    ret,thresh = cv2.threshold(img,127,255,0)
    contours,hierarchy = cv2.findContours(thresh, 1, 2)


    #--------------------------------------------------- finding puddle pixel

    print("Number of contours in image:",len(contours))
    print()

    count = len(contours)

    sum = 0
    i=0

    while (i<count):
        cnt = contours[i]
        M = cv2.moments(cnt)
        area = cv2.contourArea(cnt)
        if (area>0):
            sum += area
        i+=1


    print("puddle pixel: ", sum)
    print()

    #--------------------------------------------------- finding total pixel

    def get_num_pixels(filepath):
        width, height = Image.open(filepath).size
        return width*height

    tot = get_num_pixels(dirpath)

    print("total pixel: ", tot)
    print()


    ratio = sum/tot

    print("ratio of the image: ", '%.2f' % ratio)
    print()

    #---------------------------------------------------

    if (0 < ratio <= 0.25):
        water_level = 1
    elif(0.25 < ratio <= 0.5):
        water_level = 2
    elif(0.5 < ratio <= 0.75):
        water_level = 3
    elif(0.75< ratio <= 1):
        water_level = 4

    print("water level: ", water_level)
    print()

import serial

arduino = serial.Serial(port = 'com3', baudrate = 9600)

command = str(water_level)
arduino.write(command)
