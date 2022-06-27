#writing records from a csv file
import csv
F=open("D:\\12th File handle\\petcare.csv","a",newline="")
w=csv.writer(F)
rec=[]
while True:
    num=input("num")
    name=input("name")
    age=input("age")
    data=[num,name,age]
    rec.append(data)
    ch=input("y\n")
    if ch=="n":
        break
w.writerow(["num","name","age"])
w.writerows(rec)
F.close()


#reading records from a csv file:
import csv
F=open("D:\\12th File handle\\petcare.csv","r",newline="")
r=csv.reader(F)
for i in r:
    print(i)    
