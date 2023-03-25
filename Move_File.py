import os

from_dir = "C:/Users/DELL/Downloads"
to_dir = "C:/Users/DELL/Desktop/Neil/Coding/Python/Project_111/Document_Files"

list_of_files = os.listdir(from_dir)
#print(list_of_files)

for i in list_of_files:
    name, ext = os.path.splitext(i)
    print(name, '\t', ext)