import os
import shutil

# file detection
# path_parent = 'C:\\Users\\juice\\Desktop'
# path_file = 'C:\\Users\\juice\\Desktop\\address.txt'
# path_folder = 'C:\\Users\\juice\\Desktop\\trade stuff'

# if os.path.exists(path_parent):
#     print("that loation exists")
#     if os.path.isfile(path_file):
#         print("path is a file")
#     elif os.path.isdir(path_folder):
#         print("is a directory")
# else:
#     print("that path doesn't exist!")


###############################
# reading files
# try:
#     with open('test.txt') as file:
#         print(file.read())
# except FileNotFoundError as e:
#     print(e)
#     print('this file was not found :(')
################################
# writing file
with open('test2.txt', 'w') as file:
    file.write("hello how are you?\nyou good bro?\nokay cool\n")

    if os.path.isfile('test2.txt'):
        with open('test2.txt','a') as file2:
            file.write("last name Taylor")

with open('test2.txt') as file:
         print(file.read())

##################
#copy files
#copyfile() = copies content of a file
#copyfile() = copyfile() + permission mode + destination can be a directory
#copy2() = copy() +  copies metadata (file's creation and modification times)

shutil.copyfile('text.txt','text_copy.txt')

########################
#moving files

# src = "text_copy.txt"
# destination = "C:\\Users\\juice\Desktop\\text_copy.txt"


# try:
#     if os.path.exists(destination):
#         print('file alread exists')
#     else:
#         os.replace(src,destination)
#         print('file moved successfully')
# except FileNotFoundError as e:
#     print(e)

##################

#deleting files
#os.remove(path) remove file 
#os.rmdir(path) remove only empty folders
#shutil.rmtree(path) remove folder that contain files

path  = ''

try:
    os.remove(path)
    # os.rmdir(path)
    #shutil.rmtree(path)
except  FileNotFoundError:
    print('that file was not found')
except PermissionError:
    print("you do not have permission to delete that file")
except OSError:
    print("you can't delete a dirtree with that os.rmdir(path) method")
else:
    print('path was deleted')
