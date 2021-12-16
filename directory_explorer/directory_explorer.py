#program that deletes files within a given directory and its accompanying sub-directories, while preserving the folder structure

import os
import sys

def directory_checker(a_path):	#function that recursively checks if given path is a directory or a file and deletes if path is a file
	a_path=os.path.abspath(a_path)  #obtain the absolute file path
	if  (os.path.isfile(a_path)):
		os.unlink(a_path)	#permanently delete file (in order to move to recycle bin, change 'unlink' to remove)
		print('removed',a_path)
	elif (os.path.isdir(a_path)):
		folders=os.listdir(a_path)	#expand folder
		print('passed',a_path)
		for item in folders:
			filepath = os.path.join(a_path, item)	#develop valid file path
			directory_checker(filepath)	#function calls itself in order to expand encountered folder structure
	return





dir=input("Enter a valid path to the directory you wish to remove files: ")
dir=dir.replace('\\','/')	#replace the backslash with forward slash in the case of Windows environment
#syntax: str.replace(old,new[,max])

dir=dir.strip('\"')	#remove double quotes eg- consider the classic case where user copy pastes path
dir=dir.strip("\'")	#remove single quotes
confirm=input("all files in the directory and subdirectories will be deleted.\n Proceed? \n Press \"n\" then 'Enter/Return' key to abort or press 'Enter/Return' key to continue\n")

if (confirm=='n'):
	sys.exit()
else:
	directory_checker(dir)



