import os

def rename_file(old_name, new_name):
    try:
        os.rename(old_name, new_name)
        print(f"File '{old_name}' has been renamed to '{new_name}'.")
    except FileNotFoundError:
        print(f"Error: The file '{old_name}' does not exist.")
    except FileExistsError:
        print(f"Error: A file with the name '{new_name}' already exists.")
    except Exception as e:
        print(f"An error occurred: {e}")

def train(roboflow_path, dataset_name):
    train_img = os.path.join(roboflow_path, "train", "images")
    train_lab = os.path.join(roboflow_path, "train", "labels")
    
    train_img_files = os.listdir(train_img)
    train_lab_files = os.listdir(train_lab)
    
    # Rename files in the train/images directory
    a = 0
    for file in train_img_files:
        _, extension = os.path.splitext(file)
        old_file_path = os.path.join(train_img, file)
        new_file_name = f"{dataset_name}_{file}_{a}{extension}"
        new_file_path = os.path.join(train_img, new_file_name)
        rename_file(old_file_path, new_file_path)
        a += 1

    # Reset the counter for the train/labels directory
    a = 0
    for file in train_lab_files:
        _, extension = os.path.splitext(file)
        old_file_path = os.path.join(train_lab, file)
        new_file_name = f"{dataset_name}_{file}_{a}{extension}"
        new_file_path = os.path.join(train_lab, new_file_name)
        rename_file(old_file_path, new_file_path)
        a += 1

# Example usage
#train(r"C:\Users\HP\Documents\sebastian data\program files\dtaseaaaaaaaaaaaaaaaaaaaaaa\dataset", "secomd")

def valid(roboflow_path, dataset_name):
    valid_img = os.path.join(roboflow_path, "valid", "images")
    valid_lab = os.path.join(roboflow_path, "valid", "labels")
    
    valid_img_files = os.listdir(valid_img)
    valid_lab_files = os.listdir(valid_lab)
    
    # Rename files in the valid/images directory
    a = 0
    for file in valid_img_files:
        _, extension = os.path.splitext(file)
        old_file_path = os.path.join(valid_img, file)
        new_file_name = f"{dataset_name}_{file}_{a}{extension}"
        new_file_path = os.path.join(valid_img, new_file_name)
        rename_file(old_file_path, new_file_path)
        a += 1

    # Reset the counter for the valid/labels directory
    a = 0
    for file in valid_lab_files:
        _, extension = os.path.splitext(file)
        old_file_path = os.path.join(valid_lab, file)
        new_file_name = f"{dataset_name}_{file}_{a}{extension}"
        new_file_path = os.path.join(valid_lab, new_file_name)
        rename_file(old_file_path, new_file_path)
        a += 1
#valid(r"C:\Users\HP\Documents\sebastian data\program files\dtaseaaaaaaaaaaaaaaaaaaaaaa\dataset","second")