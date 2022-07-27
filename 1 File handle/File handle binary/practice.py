
#Writing in a binary file:
import json
F=open("D:\\12th File handle\\Practice.dat","ab")
rec=[]
while True:
    rno=int(input("Enter the roll number of the student"))
    name=input("Enter the name of the student")
    Class=int(input("Enter the class of the student"))
    marks=float(input("Enter the marks of the student"))
    data=[rno,name,Class,marks]
    rec.append(data)
    ch=input("Do you want to enter more records? y/n")
    if ch in ["n","N"]:
        break

byte=json.dumps(rec).encode("utf-8")
F.write(byte) 
print("Data written successfully")   
F.close()

#Reading data in a binary file


try:
    F=open("D:\\12th File handle\\practice.dat","rb")
    value=pickle.load(F)
    for i in value:
        print(i[0],i[1],i[2],i[3],sep="\n")
    print("End of file")
    F.close()
except EOFError:
   
    print("End of file reached")    

#Updating records in a binary file
import pickle
try:
    F=open("D:\\12th File handle\\practice.dat","rb+")
    value=F.read()
    for i in value:
    if type(i)is bytes:
        i=i.decode()
    print(value)
    found=0
    rno=int(input("Enter the roll number of the student to update record"))
    for i in value:
        if rno==i[0]:
            print("Existing record:",i)
            marks=float(input("Enter the updated marks "))
            i[3]=marks
            print("Updated record:",i)
            found=1
        else:
            pass
    if found==0:
        print("Record not found")
    F.close()    
except EOFError:
    print("end of file reached")

#Deleting records in a binary file

F=open("D:\\12th File handle\\practice.dat","rb")
found=0
rec=[]

value=F.read()
for i in value:
    if type(i)is bytes:
        i=i.decode()
rno=int(input("Enter the roll number to delete record"))
F.close()

F=open("D:\\12th File handle\\practice.dat","wb")
for i in value:
    if i[0]==rno:
        print("Deleted record:",i)
        continue
    else:
        rec.append(i)
byte=json.dumps(value).encode("utf-8") 
F.write(byte)
F.close()   
