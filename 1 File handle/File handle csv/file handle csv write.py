#writing to a csv file:

import csv
F=open("D:\\12th File handle\\stud.csv","w",newline="") #f is the file object
w=csv.writer(F)         # w is the writer object
w.writerow(["Rno.","Name","class","Marks"]) #header row
rec=[]

while True:
    print("enter the student details")
    rno=int(input("enter the roll number of the student")) #if data type is diff we get value error
    name=input("enter the name of the student")
    Class=int(input("enter the class of the student"))
    mark=float(input("enter the mark of the student"))
    
    data=[rno,name,Class,mark] #packing process
    rec.append(data)

    ch=input("do you want to enter more records? y/n")

    if ch in "Nn":
        break
        
for i in rec:
    w.writerow(i)
    
F.close()
