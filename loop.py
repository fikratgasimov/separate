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
import csv

from PIL import Image

# Initiliaze Count and index:
count = 1
index = 1

# read roots, directories as well as files :
for root, dirs, files in os.walk('/home/fikrat/venv/lib/python3.7/site-packages/separate'):


    for files in sorted(os.listdir(os.getcwd())):

        if files.endswith(".png") and files == str(count) + "Grayscale" + ".png":
            print(files)

            img = cv2.imread(files, cv2.IMREAD_COLOR)
            image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)



            #Initialize Black and White Pixels via array
            white_pixel = np.array([255,255,255])
            black_pixel = np.array([0, 0, 0])

            # Declare Height and Width of the Shape
            height = image.shape[0]
            width = image.shape[1]




            #Loop through height and width of Original Image
            for height in range(image.shape[0]):
                for width in range(image.shape[1]):

                    # Define Pixel value of the Image
                    pixel = image[height, width]

                    # Set the if statement
                    if all(pixel != black_pixel):
                        pixel = 255
                        image[height, height] = pixel
            # determine new path
            path = 'Analyzied_Image.all'
            # save Confirmed Ground Truth Images
            cv2.imwrite(os.path.join(path, str(index) + files[9:-9] + 'Analyzed.png'), image)

    #Increment the values of the
    count = count + 1
    index = index + 1



