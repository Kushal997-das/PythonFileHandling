import pickle
def Bdelete():
    F= open("D:\\12th File handle\\studrec.dat","rb")
    stud =F.read()
    for i in stud:
        if type(i)is bytes:
            i=i.decode()
    F.close()
    print(stud)
    
    rno= int(input("Enter the roll number to be deleted"))
    F= open("D:\\12th File handle\\studrec.dat","wb")
    rec= []
    for i in stud:
        if i[0] == rno:
        continue
        rec.append(i)
    F.write(rec)
    F.close()
Bdelete()
