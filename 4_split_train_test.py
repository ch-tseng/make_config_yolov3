import random
import glob, os
import os.path

#---------------------------------------------------------
testRatio = 0.2
imageFolder = "H:/Datasets/Weight_Vegetables/yolo"
cfgFolder = "H:/Datasets/Weight_Vegetables/yolo_config"
colab_yolo_path = "/mydrive/space_Colab/dataset/Weight_Vegetables/yolo/"
#--------------------------------------------------------

fileList = []
fileList_colab = []
outputTrainFile = os.path.join(cfgFolder,"train.txt")
outputTestFile = os.path.join(cfgFolder ,"test.txt")
output_colabTrainFile = os.path.join(cfgFolder,"train_colab.txt")
output_colabTestFile = os.path.join(cfgFolder ,"test_colab.txt")

if not os.path.exists(cfgFolder):
    os.makedirs(cfgFolder)

for file in os.listdir(imageFolder):
    filename, file_extension = os.path.splitext(file)
    file_extension = file_extension.lower()

    if(file_extension == ".jpg" or file_extension==".jpeg" or file_extension==".png" or file_extension==".bmp"):
        fileList.append(os.path.join(imageFolder, file))
        fileList_colab.append(colab_yolo_path+file)

print("total image files: ", len(fileList))

testCount = int(len(fileList) * testRatio)
trainCount = len(fileList) - testCount

a = range(len(fileList))
test_data = random.sample(a, testCount)
train_data = [x for x in a if x not in test_data]

print ("Train:{} images".format(len(train_data)))
print("Test:{} images".format(len(test_data)))

with open(outputTrainFile, 'w') as the_file:
    for i in train_data:
        the_file.write(fileList[i] + "\n")
the_file.close()

with open(outputTestFile, 'w') as the_file:
    for i in test_data:
        the_file.write(fileList[i] + "\n")
the_file.close()

with open(output_colabTrainFile, 'w') as the_file:
    for i in train_data:
        the_file.write(fileList_colab[i] + "\n")
the_file.close()

with open(output_colabTestFile, 'w') as the_file:
    for i in test_data:
        the_file.write(fileList_colab[i] + "\n")
the_file.close()