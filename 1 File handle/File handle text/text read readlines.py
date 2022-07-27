F=open("D:\\12th File handle\\happy.txt","r")
value=F.readlines()
for lines in value:
    for word in lines.split():
        print(word,end="#")
F.seek(0)
result=F.read()
result= result.split()
for word in result:
    print(word,end="*")
F.close()    
