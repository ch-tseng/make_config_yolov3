import os

yolo_version = "yolov3-tiny"  #yolov3, yolov3-tiny
classList = { "v1":0, "v2":1, "v3":2, "v4":3, "v5":4, "V6":5, "v7":6, "v8":7, "v20":8, "v21":9, "v22":10, "v23":11 }
cfgFolder = "H:/Datasets/Weight_Vegetables/yolo_config"
numBatch = 32
numSubdivision = 8
anchors = "68,120, 72,264, 92,162, 130,231, 174,121, 185,291"
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