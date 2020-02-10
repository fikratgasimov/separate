import os
count = 1
for root, dirs, files in os.walk('/home/fikrat/my_name/Training_Images/ColorImage_road02/ColorImage/'File_name'/'Last Directory'):
    for files in sorted(os.listdir(os.getcwd())):
        if files.endswith(".jpg"):
            print(files)
            new_name = "Original_Image" + str(count) + ".jpg"
            os.rename(files, new_name)
            count += 1




