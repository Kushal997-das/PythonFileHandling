'''
Note**
if you append something in a existance file and your existance file keeps
some data the after append something it will not  remove your privious data
like in write().It will just append your data.
file.
'''
f1=open("demo1.txt",'a')
f2=f1.write("Hello ML intern")
f1.close()
f2=open("demo1.txt",'r')
print(f2.read())