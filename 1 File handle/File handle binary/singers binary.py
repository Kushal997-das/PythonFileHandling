import pickle
import json
F=open("D:\\12th File handle\\singers.dat","ab")
Dict={5:"BoneM",6:"Queen",7:"Cher",8:"Camila cabello",9:"back st boys",10:"venga boys",11:"Doris day",12:"ABBA"}
#pickle.dump(Dict,F)
byte=json.dumps(Dict).encode("utf-8")
F.write(byte)
F.close()

f=open("D:\\12th File handle\\singers.dat","rb")
#value=pickle.load(f)
value=f.read()
#value=bytearray(value,'utf-8')
for i in value:
    if type(i)is bytes:
        i=i.decode()
print(value)
f.close()
