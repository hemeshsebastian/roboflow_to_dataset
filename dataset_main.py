import os,glob
def check_dataset(dataset_path):
    print("checking the dataset")
    global dataset_train_img, dataset_train_lab, dataset_val_img, dataset_val_lab
    dataset_train_img = dataset_path+"\\train\\images"
    dataset_train_lab = dataset_path+"\\train\\labels"
    dataset_val_img = dataset_path+"\\valid\\images"
    dataset_val_lab = dataset_path+"\\valid\\labels"
    dataset_yaml=dataset_path+"\\data.yaml"

    if not os.path.exists(dataset_train_img):
        os.makedirs(dataset_train_img)

    if  not os.path.exists(dataset_train_lab):
        os.makedirs(dataset_train_lab)


    if  not os.path.exists(dataset_val_img):
        os.makedirs(dataset_val_img)

    if  not os.path.exists(dataset_val_lab):
        os.makedirs(dataset_val_lab)
    if not os.path.exists(dataset_yaml):
        f=open(dataset_yaml,"a")
        f.close()
if __name__=="__main__":
 check_dataset(r"C:\Users\HP\Documents\sebastian data\program files\dtaseaaaaaaaaaaaaaaaaaaaaaa\dar")