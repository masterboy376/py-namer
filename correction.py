import os

lsdir = os.listdir('./change')

for name in lsdir:
    newName = ""
    if "daily_mains_question_booklet" in name:
        newName = name.replace("daily_mains_question_booklet", "question_booklet")
        source = './change/'+name
        dest = './change/'+newName
        os.rename(source, dest)
        print(dest)