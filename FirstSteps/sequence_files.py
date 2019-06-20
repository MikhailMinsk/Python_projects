import os
import shutil

path = r''  # path to files
correctname = ''  # input correct new name
padding = 4

tmp = os.listdir(path)   # if it's file
files = []               # then append it
for i in tmp:            # to list
    if os.path.isfile(os.path.join(path, i)):
        files.append(i)

# list of files

files = os.listdir(path)  # get list of files

# separate

List = []
for i in files:  # get name of file and  extention
    name, extention = os.path.split(i)
    fullname = name
    while name[-1].isdigit():  # separate last digits in filename (file123 = file)
        name = name[:-1]
    digits = int(fullname.replace(name, ''))  # choice only  digits
    List.append(digits)  # get all digits of sequential in list
# rename files

offset = min(List) - 1  # get min digit
outfolder = os.path.join(path, correctname)

if not os.path.exists(outfolder):
    os.mkdir(outfolder)

for i, j in files:
    old = os.path.join(path, j)
    name, extention = os.path.split(j)
    newname = correctname + '_' + str(List[i] - offset).zfill(padding) + extention
    new = os.path.join(path, correctname, newname)
    if os.path.exists(new):
        os.remove(new)
    shutil.copy2(old, new)
# search missing frames

fullrange = range(min(List), max(List) + 1)
miss = []  # or use set for
for i in fullrange:
    if not i in List:
        miss.append(i)  # lost files

