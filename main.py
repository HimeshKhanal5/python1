# a="Hello World"
# for i in a:
#     print(i,"Hello World")



# a="Hello World. I am ram."
# for i in a:
#     if i!="."and i!="!":
#         print(i,end="")


# a="Hello World. I am ram."
# for i in a:
#     if i!=".":
#         print(i,end="")


# control statement
# break
# continue
# pass
# break


# n=10
# for i in range(10):
#     if i==5:
#         break
#     print(i)


# n=10
# for i in range(1000):
#     if i==500:
#         continue
#     print(i,end=" ")


# while Loop
# while <condition>:
    # <operation>

# a=0
# while a<=5:
#     print(a,"Hello World")
#     a=a+1

# a=3
# while a>=0:
#     print("Hello World")
#     a=a-1


# i=1
# n=int(input("Enter n="))
# while i<=10:
#     print(n,"*",i,"=",n*i)
#     i=i+1


# i=0
# s=0
# n=int(input("enter n="))
# while i<n:
#     x=int(input("Enter x="))
#     s=s+x
#     i=i+1

# print(s)


# i=1
# fac=1
# n=int(input("Enter n="))
# while i<=n:
#     fac=fac*i
#     i=i+1

# print(fac)

# python collection
# list
# tuple
# dict
# set


# list
# -Indexing
# -multiple and duplicate Data 
# -ordered
# -mutable


# a=list()
# a=[1,2,3,4,5,6,7,8,9,0]
# b=["Apple","ball","cat","dog","elephant"]
# print(type(a))
# print(type(b))
# print(a)
# print(b)


# print(b[0])
# print(b[0:5])
# print(b[0:5:2])


# a=[1,2,3,4,5,6,7,8,9,0]
# b=["Apple","ball","cat","dog","elephant"]
# c=a+b
# print(c)


# b=["Apple","ball","cat","dog","elephant"]
# print(b*2)


# a=[1,2,3,4,5,6,7,8,9,0]
# print(a*2)


# append() insert() extend()


# b=["Apple","ball","cat","dog","elephant"]
# b.append("ramu")
# print(b)


# create a list #


# a=[]
# n=int(input("Enter n="))
# for i in range(n):
#     x=int(input("Enter x="))
#     a.append(x)
# print(a)


# print("min value=",min(a))
# print("max value=",max(a))
# print("sum value=",sum(a))
# a.sort()
# print(a)
# a.reverse()
# print(a)


# b=["Apple","ball","cat","dog","elephant"]
# a=[1,2,3]
# b.extend(a)
# print(b)


# b=["Apple","ball","cat","dog","elephant"]
# b[0:2]=["ram","sam"]
# print(b)


# del remove() pop()

# a=["Apple","ball","cat","dog","elephant"]
# del a[0:3]
# print(a)


# a=["Apple","ball","cat","dog","elephant"]
# a.remove("ball")
# print(a)


# a=["Apple","ball","cat","dog","elephant"]
# b=a.pop(0)
# print(a)
# print(b)


# a=["Apple","ball","cat","dog","elephant"]
# for i in a:
#     print(i)


# a=["Apple","ball","cat","dog","elephant"]
# print(len(a))


# i=0 
# a=["Apple","ball","cat","dog","elephant"]
# l=len(a)
# print(l)
# while i<l:
#     print(a[i])
#     i=i+1


# list inside list
# l=[[1,2,3],
#    [4,5,6],
#    [7,8,9]]
# print(l[0])

# print(l[0][0])


# l=[["ram",20,"pathari"],
#    ["sam",40,"urlabari"]]
# print(l)


# wap to create list inside list

# info=[]
# n=int(input("Enter n="))
# for i in range(n):
#     name=input("Enter name=")
#     age=int(input("Enter age="))
#     add=input("Enter add=")
#     info.append([name,age,add])
# print(info)


# l=[["ram",20,"pathari"],
#    ["sam",40,"urlabari"]]
# l[0]=["ramu",55,"ktm"]
# print(l)


# # scarch
# l=[["ram",20,"pathari"],["sam",40,"urlabari"]]
# for i in l:
#     print(i)

# name=input("Enter name=")
# for i in l:
#     if name in i:
#         print(i)


# l=[["Ram",20,"Pathari"],["Sam",40,"Urlabari"],["Ramu",20,"Pathari"]]
# name=input("Enter name=")
# for i in l:
#     if name.lower() in i[0].lower():
#         print(i)


# WAP to remove multiple or duplicate data from list?
# l=["Apple","Ball","Cat","Apple"]
# WAP to find index of duplicate data?
# l=["Apple","Ball","Cat","Apple"]


# l = ["Apple", "Ball", "Cat", "Apple"]
# unique_list = list(set(l))
# print("The list after removing duplicates:", unique_list)


###dictionary
# indexing
# multiple and duplicate Value
# ordered
# mutable

# d={<key>:<value>,<key>:<value>}

# d={'a':'Apple','b':'Ball'}
# print(d)
# print(type(d))
# print (d['a'])


# WAP to create dict using name and phone number?
# d={}
# n=int(input("Enter n="))
# for i in range(n):
#     name=input("Enter name=")
#     phone=input("Enter phone=")
#     d[name]=phone
# print(d)

# for i in d:
#     print(i)

# for i in d.values():
#     print(i)

# for i in d.items():
#     print(i)

# in dict no + *

# d={'Ram':[989898989898,980000000],'Sam':[97023366,98989898]}
# print(d['Ram'][1])

# edit###
# d={'Ram':[989898989898,980000000],'Sam':[97023366,98989898]}
# d['Ram'][0]=98989898
# print(d)

# ####del
# del d['Ram'][1]
# print(d)


# d={'name':[],
#    'age':[],
#    'add':[]}
# n=int(input("Enter n="))
# for i in range(n):
#     name=input("Enter name=")
#     age=int(input("Enter age="))
#     add=input("Enter add=")
#     d['name'].append(name)
#     d['age'].append(age)
#     d['add'].append(add)
# print(d)


# print(d['name'][0])
# print(d['age'][0])
# print(d['add'][0])

# del(d['name'][0])
# del(d['age'][0])
# del(d['add'][0])
# print(d)



# l=[]
# n=int(input("Enter n="))
# for i in range(n):
#     name=input("Enter name=")
#     age=int(input("Enter age="))
#     add=input("Enter add=")
#     d-{'name':name,'age':age,'add':add}
#     l.append(d)
# print(l)




# t=(1,)
# print(type(t))


