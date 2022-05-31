import json 
import pickle 
import numpy as np


dict = {"Programa": "wsp"}
dict["Programa"]="wspz","words","ppt"
   

with open('data.json', 'w') as fp:
    json.dump(dict, fp)


arr = []
while True:
    hola=int(input())
    if hola >=1:
        arr.append(hola)
        break
    break

with open('test2.pkl','wb') as f:
    pickle.dump(arr, f)
    
lectura = []

with open('test2.pkl','rb') as f:
        x = pickle.load(f)
        lectura.append(x)
        print(lectura)
        print(x,"Esto es sin el array")
