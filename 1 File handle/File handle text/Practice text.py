F=open("D:\\12th File handle\\happy.txt","r")
val=F.readlines()
print(val)
print(F.tell())
F.seek(0)
value=F.read()
print(value)
F.close()