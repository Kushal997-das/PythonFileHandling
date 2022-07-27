#Updating records in a binary file
import json

def update():
    F=open("D:\\12th File handle\\class.dat",'rb+')
    S=F.read()
    for i in S:
    if type(i)is bytes:
        i=i.decode()
    print(S)
    found=0
    rno=int(input("enter the roll number you want to update"))
    for i in S:
        if rno==i[0]:
            print("the currrent name is",i[1])
            i[1]=input("enter the new name")
            found=1
            break

    if found==0:
        print("Record not found")

    else:
       F.seek(0)
       byte=json.dumps(S).encode("utf-8")
       F.write(byte)

     F.close()    

update()

F=open("D:\\12th File handle\\class.dat","rb")
val=F.read()
for i in val:
    if type(i)is bytes:
        i=i.decode()
print(val)
F.close()
