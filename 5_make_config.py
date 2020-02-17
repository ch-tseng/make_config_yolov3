import os

#-------------------------------------------------------------
#Same with you defined in 1_labels_to_yolo_format.py
classList = { "mask":0 }
cfgFolder = "/home/pi/training/mask_dataset/yolo_config"
colab_yolo_path = "/mydrive/space_Colab/training/yolo/"
colab_config_path = "/mydrive/space_Colab/training/yolo_config/"

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
