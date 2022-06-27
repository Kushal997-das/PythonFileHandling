import pickle
F=open("D:\\12th File handle\\singers.dat","ab")
Dict={5:"Boney.M",6:"Queen",7:"Cher",8:"Camila cabello",9:"back st boys",10:"venga boys",11:"Doris day",12:"ABBA"}
pickle.dump(Dict,F)
F.close()

f=open("D:\\12th File handle\\singers.dat","rb")
value=pickle.load(f)
print(value)
f.close()