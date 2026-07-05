# Tuples and dictionary

# Tuples
#1. Tuples are the immutable data type
#2. Stores the values in ordered format
#3. Can contain different datatypes
#4 tuples are declared in () parenthesis
#5. tuples are faster than lists

a=1,2,3,4,5
print(a)
print(type(a))

b=()
print(type(b))
b=(12) # it will be a integer datatype

c=(12,) # whenever we declare the tuple with the single element we have to put comma after the element

print(type(b))

print(type(c))

e= tuple()#tuple function 
e=()
print(type(e))

d=tuple([1,2,3,4,5,'Sumit','Gaurav',3.14,'a'])
print(d)

# # traversing the tuples
for i in d:
    print(i)

# # slicing in the tuples
print(d[::-1])
print(d[:4])
print(d[1:7])
print(d[8:2:-2])

# d.add(12)
# d.pop()


# Dictionary
#1. Dictionary are the mutable data type
#2. Stores the values in KEY:VALUE pairs
#3. Can contain different datatypes
#4 Dictionaries are declared in {} parenthesis


d={}#for creating the empty dictoniary 
print(type(d))

e=dict()# dictoniary function 
print(type(e))

a={'Name':'Palwinder','Age':25,'City':'Ludhiana','Height':5.11}
print(a)
print(a['Name'])#for accessing the value we want to print the key

print(a.keys())#gives only keys 
print(a.values())#gives only values
print(a.items())#gives tuples 

a.get('agee',"Not Avaliable")#if the key is not in the dictoniary print the not avaliable 
print(a)
# # traversing the dictionaries
for i,j in a.items():
    # print(i,"-- ",j)
    print(f"{i} -- {j}")

print(len(a))

# creating the dictionary from the user input
e={}
n=int(input("Enter the lenght of the dictionary :"))
for i in range(n):
   key=input("Enter the key :")
   value=input("Enter the value :")
   e[key]=value

print(e)

#same method for adding and updating 
# Updating the elements in the dictionary
a={'Name':'Palwinder','Age':25,'City':'Ludhiana','Height':5.11}
print(a)
a['Name']='Aman'
# print("After updation: ")
print(a)
a.update({'Name':'Sumit','Age':26})
# print("After updation: ")
print(a)

# # Adding elements in the dictionary
a.update({'Name':'Sumit','Scholar':'Yes'})
print(a)
a['College']='MRSPTU'
print(a)


# # Deleting elements from the dictionary
a.pop('Scholar')
print(a)
a.popitem()#delete the last key value
print(a)
del a['City'],a['Name']
print(a)
a.clear()
print(a)

d={'Name':['Palwinder','Harjot','Sumit','Nitya'],'Age':[25,26,27,28]}
print(d)

print(d['Name'][0])
for i in range(len(d['Name'])):
    print(f"{d['Name'][i]} -- {d['Age'][i]}")


#2d dict 
x = {'name':{'Firstname':'Anmol','lastname':'Singh'},'age':17,'adress':{'temp':'mohali','perm':'Talwara'}}
print(x['name'])
print(x['name']['Firstname'])