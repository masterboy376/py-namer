import os

lsdir = os.listdir('./change')

for name in lsdir:
    words = name.split('_')
    # dpp
    newFolder = words[1].split('.')[0]
    # rest
    # newFolder = words[1]+"_"+words[2].split('.')[0]
    source = './change/'+name
    dest = '../e/'+newFolder+"/"+name
    os.rename(source, dest)
    print(dest)