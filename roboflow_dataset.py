import os
import glob
#C:\Users\HP\Documents\sebastian data\program files\dtaseaaaaaaaaaaaaaaaaaaaaaa\dataset\valid\images
def check_roboflow_dataset(path):
    global train_img, train_lab, val_img, val_lab
    train_img = path+"\\train\\images"
    train_lab = path+"\\train\\labels"
    val_img = path+"\\valid\\images"
    val_lab = path+"\\valid\\labels"

    if os.path.exists(train_img):
        pass
    else:
        print("Error: train images not found")
        return 0

    if os.path.exists(train_lab):
        pass
    else:
        print("Error: train labels not found")
        return 0

    if os.path.exists(val_img):
        pass
    else:
        print("Error: valid images not found")
        return 0

    if os.path.exists(val_lab):
        pass
    else:
        print("Error: valid labels not found")
        return 0
    global yaml_path
    yaml_path = ""
    directory_path = path
    extension = "yaml"  # Change this to the desired file extension
    files = glob.glob(os.path.join(directory_path, f"*.{extension}"))

    if files:
        for file in files:
            yaml_path = file
    else:
        print("Error: yaml file missing")
    return 1
#if check_roboflow_dataset(r"C:\Users\HP\Documents\sebastian data\program files\dtaseaaaaaaaaaaaaaaaaaaaaaa\dataset"):
   # print("no problem")
