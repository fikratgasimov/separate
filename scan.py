import array as rr
import random
import cv2
from PIL import Image
import PIL
import os
from math import sqrt
import numpy
import math
import glob
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
from pandas import DataFrame
from array import *
import re
#Cutting images by white pixels
count = 1
for root, dirs, files in os.walk('/home/fikrat/venv/lib/python3.7/site-packages/separate'):

    for files in sorted(os.listdir(os.getcwd())):
        if files.endswith(".png") and files == "File" + str(count) + ".png":

        # for dirname in sorted(files):

        # if dirname.endswith('.png') and dirname.find(str(count),0,5):
            #print(dirname)
            print(files)
           # sorted(dirname)
            image = cv2.imread(files, cv2.IMREAD_COLOR)
            #whitepixel = [255, 255, 255]
            #pixels = np.array([],[])
            #output = str(1)
            cut_height = image.shape[0]
            arrays = []
            pixel = [[], []]
            whitepixel = [255, 255, 255]
            for height in range(image.shape[0]):
                for width in range(image.shape[1]):
                    pixel = image[height, width]
                    if pixel[0] == 255 and pixel[1] == 255 and pixel[2] == 255:
                       # print(pixel)
                    #if pixel.all == whitepixel:
                        if height < cut_height:
                            cut_height = height

            cropped_image = image[0:cut_height,0:3384]
            path = 'Record048'
            cv2.imwrite(os.path.join(path,files[4:-4] + 'Cropped.png'), cropped_image)
            count = count + 1


            print(cut_height)
            #print(dirname[3:-3])
                    #
                    # if pixel.all == [255, 255, 255]:
                    #     arrays.append(pixel)
                    # else:
                    #
                    # else:
                    #     continue
                    # print(arrays)






            #

                    #if pixels[height, width] == (whitepixel):
                     #   if height > cut_height:
                      #      cut_height = height
        #print(cut_height)






