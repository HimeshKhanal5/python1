# file=open(<file_name>,<mode>)
# file.close()
# with open(<file name>,<mode>) as file:
#     <operation>
# Mode 
# create mode >x
# read mode>r
# write mode>w
# append mode>a

# file=open('data.txt','x')
# file.close()

# file=open('data.txt','r')
# x=file.read()
# print(x)
# file.close()


# info=""
# n=int(input('Enter n='))
# for i in range (n):
#     name=input('Enter name=')
#     price=int(input('enter price='))
#     qty=int(input('Enter qty='))
#     total=price+qty
#     info=info+f"{name}{price}{qty}{total}\n"
# print (info)

# file=open ('bill.txt','w')
# file.write(info)
# file.close()

# info=""
# n=int(input('Enter n='))
# for i in range (n):
#     name=input('Enter name=')
#     price=int(input('enter price='))
#     qty=int(input('Enter qty='))
#     total=price+qty
#     info=info+f"{name} {price} {qty} {total}\n"
# print (info)

# file=open ('bill1.txt','a')
# file.write(info)
# file.close() 

# info=""
# n=int(input('Enter n='))
# for i in range (n):
#     name=input('Enter name=')
#     price=int(input('enter price='))
#     qty=int(input('Enter qty='))
#     total=price+qty
#     info=info+f"{name},{price},{qty},{total}\n"
# print (info)

# file=open ('bill.csv','w')
# file.write(info)
# file.close() 


# info=""
# n=int(input('Enter n='))
# for i in range (n):
#     name=input('Enter name=')
#     price=int(input('enter price='))
#     qty=int(input('Enter qty='))
#     total=price+qty
#     info=info+f"{name},{price},{qty},{total}\n"
# print (info)

# file=open ('bill.csv','w')
# file.write(info)
# file.close() 

# file=open('bill.csv','r')
# data=file.read()
# file.close()
# l=data.split('\n')[0:-1]
# l
# final_data=[]
# for i in l:
#     final_data.append(i.split(','))
# final_data

# import csv
# file=open('bill.csv','w')
# x=csv.writer(file)
# x.writerows(final_data)
# file.close()
















