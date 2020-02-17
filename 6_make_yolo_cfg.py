import os

yolo_version = "yolov3-tiny"  #yolov3, yolov3-tiny
classList = { "mask":0 }
cfgFolder = "/home/pi/training/mask/yolo_config"
numBatch = 32
numSubdivision = 8
anchors = "27,33, 37,47, 53,68, 82,93, 134,126"
#---------------------------------------------------------------------

classNum = len(classList)
filterNum = (classNum + 5) * 3

if(yolo_version == "yolov3"):
    fileCFG = "yolov3.cfg"
else:
    fileCFG = "yolov3-tiny.cfg"

with open(os.path.join("cfg",fileCFG)) as file:
    file_content = file.read()
file.close

file_updated = file_content.replace("{BATCH}", str(numBatch))
file_updated = file_updated.replace("{SUBDIVISIONS}", str(numSubdivision))
file_updated = file_updated.replace("{FILTERS}", str(filterNum))
file_updated = file_updated.replace("{CLASSES}", str(classNum))
file_updated = file_updated.replace("{ANCHORS}", anchors)

file = open(os.path.join(cfgFolder,fileCFG), "w")
file.write(file_updated)
file.close
