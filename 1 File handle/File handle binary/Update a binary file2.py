#updating records in a bnary file

import json

def update():
    F=open("D:\\12th File handle\\studrec.dat","rb+")
    value=F.read()
    for i in value:
    if type(i)is bytes:
        i=i.decode()
    print(value)
    found=0
    roll=int(input("Enter the roll number of the record"))
    for i in value:
        if roll==i[0]:
            print("current name", i[1])
            print("current marks", i[2])
            i[1]=input("Enter the new name")
            i[2]=int(input("Enter the new marks"))
            found=1

    if found==0:
        print("Record not found")

    else:
        byte=json.dumps(value).encode("utf-8")
        F.write(byte)
        F.seek(0)
        newval=F.read()
        print(newval)
        
    F.close()
update()

    
