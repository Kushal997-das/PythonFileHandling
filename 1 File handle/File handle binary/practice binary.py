'''#reading a binary file:
import pickle
F=open("D:\\12th File handle\\class.dat","rb")
value=pickle.load(F)
for i in value:
    print(i)
F.close()

#Writing to a binary file:
import pickle
F=open("D:\\12th File handle\\employees.dat","ab")
rec=[]
while True:
    Eno=int(input("Enter the employee number"))
    name=input("enter the name of employee")
    age=int(input("Enter the age of the employee"))
    data=[Eno,name,age]
    rec.append(data)
    y=input("do you want to quit?,n")
    if y=="n":
        break
pickle.dump(rec,F)
F.close()
'''
'''
#Update records in a binary file:
import pickle
F=open("D:\\12th File handle\\studrec.dat","rb+")
val=pickle.load(F)
count=0
print(val)
eroll=int(input("enter the roll number to update rec"))
for i in val:
    if i[0]==eroll:
        print(i[1], "is the current name")
        name=input("enter the new name")
        i[1]=name
        print("record updated")
        count+=1
if count==0:
    print("get off")
'''

