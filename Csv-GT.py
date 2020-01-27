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

# initialize all RGB colors and Labels via TrainId and corresponding Label name

rows = ['0 0 0','0','void','Void']
rows1 = ['70 130 180','1','s_w_d','Dividing']
rows2 = ['220 20 60','2','s_y_d','Middle Parallel line']
rows3 = ['128 0 128','3','ds_w_dn','Right line Parking']
rows4 = ['255 0 0','4','ds_y_dn','Border Line']
rows5 = ['0 0 60','5','sb_w_do','Continuous Line']
rows6 = ['0 60 100','6','sb_y_do','Right Turn']
rows7 = ['0 0 142','7','b_w_g','Guiding']
rows8 = ['119 11 32','8','b_y_g','Left Dashline']
rows9 = ['244 35 232','9','db_w_g','Cycle line']
rows10 = ['0 0 160','10','db_y_g','Thick guide Line']
rows11 = ['153 153 153','11','db_w_s','Stopping']
rows12 = ['220 220 0','12','s_w_s','Convergence Line']
rows13 = ['250 170 30','13','ds_w_s','Safety line']
rows14 = ['102 102 156','14','s_w_c','Left-Right Dash Separated Line']
rows15 = ['128 0 0','15','s_y_c','Chevron',]
rows16 = ['128 64 128','16','s_w_p','Fork Arrow']
rows17 = ['238 232 170','17','s_n_p','Turn-Left Line']
rows18 = ['190 153 153','18','c_wy_z','ZebraCrossing']
rows19 = ['0 0 230','19','a_w_u','DoubleTurn']
rows20 = ['128 128 0','20','a_w_t','Straight Arrow']
rows21 = ['128 78 160','21','a_w_tl','Continuous Line']
rows22 = ['150 100 100','22','a_w_tr','Circle Turn']
rows23 = ['255 165 0','23','a_w_tlr','Yield Sign without Words']
rows24 = ['180 165 180','24','a_w_l','TurnLeft']
rows25 = ['107 142 35','25','a_w_r','Three Merged Lines']
rows26 = ['201 255 229','26','a_w_lr','Double Turn']
rows27 = ['0 191 255','27','a_n_lu','Straight Line']
rows28 = ['51 255 51','28','a_w_tu','Right Arrow']
rows29 = ['250 128 114','29','a_w_m','Pedestrian stand Line']
rows30 = ['127 255 0','30','a_y_t','Turn Right']
rows31 = ['255 128 0','31','b_n_sr','Reduction']
rows32 = ['0 255 255','32','d_wy_za','Attention']
rows33 = ['178 132 190','33','r_wy_np','No Parking',]
rows34 = ['128 128 64','34','vom_wy_n','Turn Allowance Line']
rows35 =['102 0 204','35','om_n_n','Parking']
rows36 = ['0 153 153','255','noise','Curve Sign']
rows37 = ['255 255 255','255','ignored','Ignored']
filename = 'Color_Label.csv'
with open(filename,'w') as f:
    writer = csv.writer(f)
    writer.writerow(rows)
    writer.writerow(rows1)
    writer.writerow(rows2)
    writer.writerow(rows3)
    writer.writerow(rows4)
    writer.writerow(rows5)
    writer.writerow(rows6)
    writer.writerow(rows7)
    writer.writerow(rows8)
    writer.writerow(rows9)
    writer.writerow(rows10)
    writer.writerow(rows11)
    writer.writerow(rows12)
    writer.writerow(rows13)
    writer.writerow(rows14)
    writer.writerow(rows15)
    writer.writerow(rows16)
    writer.writerow(rows17)
    writer.writerow(rows18)
    writer.writerow(rows19)
    writer.writerow(rows20)
    writer.writerow(rows21)
    writer.writerow(rows22)
    writer.writerow(rows23)
    writer.writerow(rows24)
    writer.writerow(rows25)
    writer.writerow(rows26)
    writer.writerow(rows27)
    writer.writerow(rows28)
    writer.writerow(rows29)
    writer.writerow(rows30)
    writer.writerow(rows31)
    writer.writerow(rows32)
    writer.writerow(rows33)
    writer.writerow(rows34)
    writer.writerow(rows35)
    writer.writerow(rows36)
    writer.writerow(rows37)


filename = 'Color_Label.csv'
with open(filename, 'r') as input_file:
    reader = csv.reader(input_file)
    # Prepare Dictionary so as to provide Labelization
    mydict = {rows[0] : rows[1] for rows in reader}
    for keys,values in mydict.items():
        print(keys, '\t', values, '\n')



    # Prepare Dictionary so as to provide labelization
    mydict = {rows[0] : rows[1] for rows in reader}


 'This code analysis prepare GroundTruth Images for our goals'###############################
        count = 181
        index = 181

        for root, dirs, files in os.walk('/home/fikrat/venv/lib/python3.7/site-packages/separate'):
            for files in sorted(os.listdir(os.getcwd())):
                if files.endswith(".png") and files == str(count) + "Cropped" + ".png":

                    img = cv2.imread(files, cv2.IMREAD_COLOR)
                    image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                    height = image.shape[0]
                    width = image.shape[1]

                    # Prepare Groundtruth images
                    new_image = np.zeros([height, width], dtype=np.uint8)
                    # Loop through images by height and width
                    for h in range(height):
                        for w in range(width):
                            # take color from original image
                            pixel = image[h, w]
                            # prepare the key string
                            color = str(pixel[0]) + ' ' + str(pixel[1]) + ' ' + str(pixel[2])

                            # use the key to access the dictionary and recover trainId
                            trainId = mydict[color]

                            # put in new image the trainId as value in the right position
                            new_image[h, w] = trainId

                    path = 'Grayscale_Images.048.6'
                    cv2.imwrite(os.path.join(path, str(index) + files[7:-7] + 'Grayscale.png'), new_image)




            count = count + 1

            index = index + 1
######################################### FINISHED THE CODE ANALYSIS################################

