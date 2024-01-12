import os
def update_yaml(path):
    s=os.path.join(path,"data.yaml")
    f=open(s,"w")
    f.write("train: path os the file\nvalid: path of the file\n")
    fo=open("index.txt")
    data=fo.readlines()
    f.write("nc: "+str(len(data)))
    f.write("\nnames:\n")
    for i in data:
        f.write(" "+str(data.index(i))+": "+i+"\n")
    f.close()
    fo.close()
#update_yaml(r"C:\Users\HP\Documents\sebastian data\program files\dtaseaaaaaaaaaaaaaaaaaaaaaa\dataset")
