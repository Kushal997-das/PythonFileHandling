'''Note**
if you write something in a existance file and your existance file keeps
some data the after writing something it will be remove your privious data and meanwhile it will append new data from that
file.

close() is must in write() because if you write something and you want to make
changes and you don't use close() as a result you're unable to do changes.
'''



#Here we see how to write a file
'''
write() : Inserts the string str1 in a single line in the text file
Syntax:File_object.write(str1)
'''
f1=open("demo1.txt","w")
f2=f1.write("Hello data science intern")
f1.close()
f2=open("demo1.txt",'r')
print(f2.read())

'''
writelines() : For a list of string elements, each string is inserted in the text file. Used to insert multiple strings at a single time.
File_object.writelines(L) for L = [str1, str2, str3] 
'''

f1=open("demo1.txt","w")
l=["I love to do python programming\n","I love to do cpp as well\n"]
f2=f1.writelines(l)
f1.close()
f2=open("demo1.txt",'r')
print(f2.read())