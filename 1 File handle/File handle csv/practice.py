#Python program to write in a csv file
import csv
try:
    F=open("D:\\12th File handle\\sample.csv","a")
    w=csv.writer(F)
    rec=[]
    while True:
        rno=input("Enter the roll number of the student")
        name=input("Enter the name of the student")
        marks=input("Enter the marks of the sudent")
        Class=input("Enter the class of the student")
        data=[rno,name,marks,Class]
        rec.append(data)
        ch=input("Do you want to enter more records?y/n")
        if ch in ("n","N"):
            break
        else:
            pass
    w.writerows(rec) 
    F.close()

except EOFError:
    print("pass")

#reading from a csv file:
import csv

try:
    F=open("D:\\12th File handle\\petcare.csv","r")
    r=csv.reader(F)
    for i in r:
        print(i,end="*")
    F.close()    
except EOFError:
    print("pass")       
