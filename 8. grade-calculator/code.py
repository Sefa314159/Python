def grade_calculate(line):
    line    =   line[:-1]
    lst     =   line.split(",")
    name    =   lst[0]
    midterm1=   int(lst[1])
    midterm2=   int(lst[2])
    final   =   int(lst[3])
    grade   =   midterm1*0.3+midterm2*0.3+final*0.4

    if(grade    >=  85):
        note    =   "AA"
    elif(grade  >=  70):
        note    =   "BA"
    elif (grade >=  60):
        note    =   "BB"
    elif (grade >=  55):
        note    =   "CB"
    elif (grade >=  50):
        note    =   "CC"
    elif (grade >=  40):
        note    =   "DC"
    elif (grade >=  30):
        note    =   "DD"
    else:
        note    =   "FF"

    return name+","+note+"\n"

def passing(line):
    line = line[:-1]
    lst     =   line.split(",")
    name    =   lst[0]
    grade   =   lst[1]
    if(grade!="FF"):
        pass1.append(name)
        pass1.append("\n")
    else:
        fail1.append(name)
        fail1.append("\n")

global pass1
pass1=[]
global fail1
fail1=[]

with open("file.txt","r",encoding="utf-8") as file:
    list1=[]
    for i in file:
        list1.append(grade_calculate(i))
with open("grades.txt","w",encoding="utf-8") as file2:
        for i in list1:
            file2.write(i)
            passing(i)
with open("passed.txt","w",encoding="utf-8") as file3:
    for i in pass1:
        file3.write(i)
with open("failed.txt","w",encoding="utf-8") as file4:
    for i in fail1:
        file4.write(i)
