'''Amit is a monitor of class XII-A and he stored the record of all
the students of his class in a file named “class.dat”.
Structure of record is [roll number, name, percentage]. His computer
teacher has assigned the following duty to Amit

Write a function remcount( ) to count the number of students who need
 remedial class (student who scored less than 40 percent)

 
 '''
#also find no. of children who got top marks

import pickle
F=open("D:\\12th File handle\\class.dat",'ab')
list=[[1,"Ramya",30],[2,"vaishnavi",60],[3,"anuya",40],[4,"kamala",30],[5,"anuraag",10],[6,"Reshi",77],[7,"Biancaa.R",100],[8,"sandhya",65]]


pickle.dump(list,F)
F.close()

def remcount():
    F=open("D:\\12th File handle\\class.dat","rb")
    val=pickle.load(F)
    count=0
    
    for i in val:
        if i[2]<=40:
            print(i,"eligible for remedial")
            count+=1
    print("the total number of students are",count)
    F.close()

remcount()

def firstmark():
    F=open("D:\\12th File handle\\class.dat",'rb')
    val=pickle.load(F)
    main=[]
    count=0
    
    for i in val:
        data=i[2]
        main.append(data)
        
    top=max(main)
    print(top,"is the first mark")

    F.seek(0)
    for i in val:
        if top==i[2]:
            print(i)
            print("congrats")
            count+=1
        
    
    print("the total number of students who secured top marks are",count)
    F.close()
firstmark()

F=open("D:\\12th File handle\\class.dat","rb")
val=pickle.load(F)
print(val)
F.close()


  
