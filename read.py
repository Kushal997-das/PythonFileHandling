#Here what we can do just read the file

#First we have to open the file for reading purpose.

f1=open("demo.txt","r")#Here i open the demo.txt file.

'''
read() : Returns the read bytes in form of a string. Reads n bytes,
if no n specified, reads the entire file.
Syntax: File_object.read([n])
'''
print('Here is the output of read()=\n',f1.read())#here i read all the documents from the demo.txt file and print it.

'''
readline() : Reads a line of the file and returns in form of a string.
For specified n, reads at most n bytes.
However, does not reads more than one line,
even if n exceeds the length of the line.
Syntax : File_object.readline([n])
'''
f2=open("demo.txt",'r')
print('Here is the output of readline()=\n',f2.readline())#it will display the single line


'''
readlines() : Reads all the lines and return them as each line a string element in a list.
syntax      :File_object.readlines()
'''
f3=open("demo.txt",'r')
print('Here is the output of readlines()=\n',f3.readlines())
