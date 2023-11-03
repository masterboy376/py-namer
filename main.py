# # rest
# import os

# lsdir = os.listdir('./change')

# for name in lsdir:
#     words = name.split('__')[0].split('_')

#     newName = ""
#     for i in range(2):
#         words[i] = words[i].strip()
#         temp = words[i].split(" ")
#         lst = list(range(len(temp)))
#         # lst.reverse()
#         for j in lst:
#             if i == 0:
#                 if j==len(temp)-1:
#                     newName+=temp[j]
#                 else:
#                     newName+=temp[j][0].lower()
#                     # if(j==0):
#                     #     newName+=temp[j][1].lower()
#             else:
#                 # if j==1:
#                 #     newName=newName.replace('_',temp[j].lower()+'_')
#                 # else:
#                 # if j==0:
#                 #     newName+=temp[j].lower()
#                 # else:
#                 newName+="_"+temp[j].lower()
#     newName+='.pdf'
#     source = './change/'+name
#     dest = './change/'+newName
#     os.rename(source, dest)
#     print(newName)




# dpp
import os

lsdir = os.listdir('./change')

for name in lsdir:
    words = name.split('__')[0].split('_')

    newName = ""
    for i in range(2):
        words[i] = words[i].strip()
        temp = words[i].split(" ")
        lst = list(range(len(temp)))
        if i!=0:
            lst.reverse()
        for j in lst:
            if i == 0:
                if j==len(temp)-1:
                    newName+=temp[j]+"_"
                else:
                    newName+=temp[j][0].lower()
            else:
                # if j==1:
                #     newName=newName.replace('_',temp[j].lower()+'_')
                # else:
                if j==0:
                    newName+=temp[j].lower()
                else:
                    newName+=temp[j].lower()+"_"
    newName+='.pdf'
    source = './change/'+name
    dest = './change/'+newName
    os.rename(source, dest)
    print(newName)