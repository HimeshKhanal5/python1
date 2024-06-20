info=""
n=int(input('Enter n='))
for i in range (1,n+1):
    name=input('Enter name=')
    age=int(input('Enter age='))
    add=input('Enter add=')
    phone=int(input('Enter phone='))
    info=info+f"{name},{age},{add},{phone}\n"
file=open("info.csv","w")
file.write("sn,name,age,add,phone\n")
file.write(info)
file.close()

import panda as pd
df=pd.read_csv('info.csv',index_col='sn')
print("df")

data={'sn':[1,2,3],
      'name':['ram','sam','hari'],
      'age':[20,30,40]}
df=pd.DataFrame(data)
df





























