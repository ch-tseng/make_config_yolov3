import random
import glob, os, sys
import os.path

#---------------------------------------------------------
saveYoloPath = "H:/Datasets/Weight_Vegetables/yolo"
output_folder = "H:/Datasets/Weight_Vegetables/"
#--------------------------------------------------------

fileList = []
outputFile = os.path.join(output_folder,"img_list.txt")

if not os.path.exists(saveYoloPath):
    print("There is no such folder for ", saveYoloPath)
    sys.exit()

for file in os.listdir(saveYoloPath):
    filename, file_extension = os.path.splitext(file)
    file_extension = file_extension.lower()

    if(file_extension == ".txt"):
        fileList.append(os.path.join(saveYoloPath, file))

trainCount = len(fileList)
print("total image files: ", trainCount)

with open(outputFile, 'w') as the_file:
    for i in range(0, len(fileList)):
        the_file.write(fileList[i] + "\n")

the_file.close()

