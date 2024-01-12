#make a bind ke yalue 
import os
def get_class_id(txt_file):#from the yaml file
    new_id = []

    with open(txt_file, 'r') as file:
        for line in file:
            if line.startswith('names:'):
                names_list = line.split('names: ')[1].strip('[]\n').split(', ')
                new_id.extend(names_list)

    new_id1=[]
    for i in new_id:
        i=i.replace("'","")
        new_id1.append(i)
    return new_id1
def get(file_path):
    my_list = []
    with open(file_path, 'r') as file:
        for line in file:
            my_list.append(line.strip())
    return my_list

def get_dict(path):
    main_id=get("index.txt")
    class_id=get_class_id(os.path.join(path,"data.yaml"))
    print(class_id)
    print(main_id)
    for i in class_id:
        if  not i in main_id:
            main_id.append(i)
    print(main_id)#make a dictionary
    f=open("index.txt","w")
    for i in main_id:
        f.write(i.replace("\n",""))
        f.write("\n")
    f.close()
    fop=open("index.txt")
    fs=fop.readlines()
    #startthe dict make:
    emp_dict={}
    for u in class_id:
        index=class_id.index(u)
        index1=main_id.index(u)
        emp_dict[str(index)]=str(index1)
    return emp_dict

def change_id_file(dictionary,filename):

	f=open(filename,"r")
	data=f.readlines()
	f.close()
	f=open(filename,"w")
	for line in data:
		token=line.split(" ")
		class_ud=token[0]
		if class_ud in dictionary:
				token[0]=dictionary[str(class_ud)]
		iu=0
		for io in token:
				f.write(io)
				if not token.index(io)==len(token)-1:
					f.write(" ")
	f. close()
def list_files (directory_path):
    files = []
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        if os.path.isfile(file_path):
            files.append(file_path)
    return files
def replace_class(path):#dataset path
      train_lan=os.path.join(path,"train")
      train_lan=os.path.join(train_lan,"labels")
      al_lan=os.path.join(path,"valid")
      al_lan=os.path.join(al_lan,"labels")
      files=list_files(train_lan)
      for file in files:
            print(file)
            train_lan=os.path.join(path,file)
            change_id_file(get_dict(path),train_lan)
      files=list_files(al_lan)
      for file in files:
            print(file)
            al_lan=os.path.join(al_lan,file)
            change_id_file(get_dict(path),al_lan)
#replace_class(r"C:\Users\HP\Documents\sebastian data\program files\dtaseaaaaaaaaaaaaaaaaaaaaaa\dataset")#dataset path of the roboflow dataset
#change_id_file(get_dict(r"C:\Users\HP\Documents\sebastian data\program files\dtaseaaaaaaaaaaaaaaaaaaaaaa\dataset"),r"C:\Users\HP\Documents\sebastian data\program files\dtaseaaaaaaaaaaaaaaaaaaaaaa\tr.txt")
#change_id_file(class_id,r"C:\Users\HP\Documents\sebastian data\program files\dtaseaaaaaaaaaaaaaaaaaaaaaa\tr.txt")
            

#replace the classid in the dataset train and alid lables
if __name__=="__main__":
 replace_class(r"C:\Users\HP\Documents\sebastian data\program files\dtaseaaaaaaaaaaaaaaaaaaaaaa\dataset")