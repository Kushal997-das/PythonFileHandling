#program to print words with length less than or equal to 4

F=open("D:\\12th file handle\\happy.txt","r")
val=F.readlines()
count=0
for line in val:
    for word in line.split(): #line.split() makes the string line into a list with its constituent words
        if len(word)<=4:
            print(word)
            count+=1

print("The total number of words are",count)      
