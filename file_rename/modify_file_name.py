#program that replaces specific charcter in file names within directory

import os
import sys

def directory_checker(a_path):  #function that recursively checks if given path is a directory or a file and deletes if path is a file
    a_path=os.path.abspath(a_path)  #get absolute path to given directory
    folders=os.listdir(a_path)  #expand folder
    for item in folders:
        filepath = os.path.join(a_path, item)   #develop valid file path
        old="%20" #string character to be removed from file names
        new=" " #string character to replace old character
        filepath2=filepath.replace(old,new)
        os.rename(filepath,filepath2)
    return





dir=input("Enter a valid path to the directory you wish to remove files: ")
dir=dir.replace('\\','/')   #replace the backslash with forward slash in the case of Windows environment
#syntax: str.replace(old,new[,max])

dir=dir.strip('\"') #remove double quotes eg- consider the classic case where user copy pastes path
dir=dir.strip("\'") #remove single quotes
confirm=input("files in the directory will be renamed.\n Proceed? \n Press \"n\" then 'Enter/Return' key to abort or press 'Enter/Return' key to continue\n")

if (confirm=='n'):
    sys.exit()
else:
    directory_checker(dir)



