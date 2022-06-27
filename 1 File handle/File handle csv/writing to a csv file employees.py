import csv
F=open("employees.csv","a",newline="")
w=csv.writer(F)
record=[]

while True:
    id_=int(input("Enter the employee id of the employee"))
    name=input("Enter the name of the employee")
    age=int(input("Enter the age of the employee"))
    gen=input("Enter the gender of the employee")
    qual=input("Enter the qualification of the employee")
    sal=float(input("Enter the salary of the employee"))

    data=[id_,name,age,gen,qual,sal]
    record.append(data)

    choice= input("Do you want to enter more records? y/n")

    if choice in ["n","N"]:
        break

w.writerows(record)    
F.close()
