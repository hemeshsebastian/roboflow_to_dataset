from roboflow_dataset import*
from dataset_main import*

from renameinput_dataset import*
from update_yaml import*
from mergee import*
from renamer import*

roboflow_path=r"C:\Users\HP\Documents\sebastian data\program files\dtaseaaaaaaaaaaaaaaaaaaaaaa\roboflowdataset"
datasetpath=r"C:\Users\HP\Documents\sebastian data\program files\dtaseaaaaaaaaaaaaaaaaaaaaaa\dataset"
dataset_name="hemesh"
#step 1
#check the roboflow dataset:
#if check_roboflow_dataset(roboflow_path):
#    print("no problem")
#step2 main dataset checking

#check_dataset(r"C:\Users\HP\Documents\sebastian data\program files\dtaseaaaaaaaaaaaaaaaaaaaaaa\dataset")
#step 3 rename the train files:
#train(roboflow_path,dataset_name)
#valid(roboflow_path,dataset_name)

#change he class id respec to to dataset
#replace_class(roboflow_path)
#update_yaml(datasetpath)
merge_dataset(roboflow_path,datasetpath)
#C:\Users\HP\Documents\sebastian data\program files\dtaseaaaaaaaaaaaaaaaaaaaaaa\roboflowdataset\train\labels