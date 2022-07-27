#Python program to print all the words of length 4 and also count such words
F=open("D:\\12th File handle\\happy.txt","r")
value=F.read()
count=0
value=value.split()
for i in value:
    if len(i)<=4:
        print(i,end="#")
        count+=1
F.close()
