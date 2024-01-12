import shutil
import os

def copy_dataset_0(source_directory, destination_directory):
    # Get a list of files in the source directory
    files_to_copy = [file for file in os.listdir(source_directory) if os.path.isfile(os.path.join(source_directory, file))]

    # Copy files with the same name from source to destination
    for file_name in files_to_copy:
        source_path = os.path.join(source_directory, file_name)
        destination_path = os.path.join(destination_directory, file_name)

        shutil.copy2(source_path, destination_path)

    print("Files copied successfully.")

# Example usage:
source_directory = r'C:\Users\HP\Documents\sebastian data\program files\dtaseaaaaaaaaaaaaaaaaaaaaaa\dataset\valid\images'
destination_directory = r'C:\Users\HP\Documents\sebastian data\program files\dtaseaaaaaaaaaaaaaaaaaaaaaa\dataset'

def merge_dataset(path,des_path):#path refers to the roboflow dataset#des path is the datset for main:
    merge_train=os.path.join(path,"train")
    merge_Valid=os.path.join(path,"valid")
    merge_train_img=os.path.join(merge_train,"images")
    merge_train_lab=os.path.join(merge_train,"labels")
    merge_Valid_img=os.path.join(merge_Valid,"images")
    merge_Valid_lab=os.path.join(merge_Valid,"labels")


    merge_train1=os.path.join(des_path,"train")
    merge_Valid1=os.path.join(des_path,"valid")
    merge_train_img1=os.path.join(merge_train1,"images")
    merge_train_lab1=os.path.join(merge_train1,"labels")
    merge_Valid_img1=os.path.join(merge_Valid1,"images")
    merge_Valid_lab1=os.path.join(merge_Valid1,"labels")

    copy_dataset_0(merge_train_img,merge_train_img1)
    copy_dataset_0(merge_train_lab,merge_train_lab1)
    copy_dataset_0(merge_Valid_img,merge_Valid_img1)
    copy_dataset_0(merge_Valid_lab,merge_Valid_lab1)

