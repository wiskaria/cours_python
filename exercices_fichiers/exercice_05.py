import os


def create_file_in_dir(file_name, dir_name):
    os.mkdir(dir_name)
    with open(dir_name+"\\"+file_name,"w") as file:
        pass

create_file_in_dir("oui.txt","haha")