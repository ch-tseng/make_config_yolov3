import os

#-------------------------------------------------------------
#Same with you defined in 1_labels_to_yolo_format.py
classList = { "v1":0, "v2":1, "v3":2, "v4":3, "v5":4, "V6":5, "v7":6, "v8":7, "v20":8, "v21":9, "v22":10, "v23":11 }
cfgFolder = "H:/Datasets/Weight_Vegetables/yolo_config"
colab_yolo_path = "/mydrive/space_Colab/dataset/Weight_Vegetables/yolo/"
colab_config_path = "/mydrive/space_Colab/dataset/Weight_Vegetables/yolo_config/"

#-------------------------------------------------------------
cfg_obj_names = "obj.names"
cfg_obj_data = "obj.data"
cfg_obj_data_colab = "obj_colab.data"
classes = len(classList)

pathCFG = os.path.join(cfgFolder, "weights")
if not os.path.exists(pathCFG):
    os.makedirs(pathCFG)
    print("all weights will generated in here: ", pathCFG)


with open(os.path.join(cfgFolder, cfg_obj_data), 'w') as the_file:
    the_file.write("classes= " + str(classes) + "\n")
    the_file.write("train  = " + os.path.join(cfgFolder ,"train.txt") + "\n")
    the_file.write("valid  = " + os.path.join(cfgFolder ,"test.txt") + "\n")
    the_file.write("names = " + os.path.join(cfgFolder ,"obj.names") + "\n")
    the_file.write("backup = " + os.path.join(cfgFolder ,"weights") + "/")
the_file.close()

with open(os.path.join(cfgFolder, cfg_obj_data_colab), 'w') as the_file:
    the_file.write("classes= " + str(classes) + "\n")
    the_file.write("train  = " + os.path.join(colab_config_path ,"train_colab.txt") + "\n")
    the_file.write("valid  = " + os.path.join(colab_config_path ,"test_colab.txt") + "\n")
    the_file.write("names = " + os.path.join(colab_config_path ,"obj.names") + "\n")
    the_file.write("backup = " + os.path.join(colab_config_path ,"weights") + "/")
the_file.close()

print("and cfg folder: " + pathCFG + " ,is ready for training.")

with open(os.path.join(cfgFolder ,cfg_obj_names), 'w') as the_file:
    for className in classList:
        the_file.write(className + "\n")
the_file.close()
