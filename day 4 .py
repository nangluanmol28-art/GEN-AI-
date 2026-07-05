#list comprehen.py
#basic syntax 
#list name = [expression for item in literable if confition]
a=[i for i in range(1,41) if i%2!=0]# printing the odd numbers 
print(a)

fruits = ['Apple','Mango','Papaya','Orange','Pineapple']
a = [i for i in fruits if len(i)>5]#print only that fruit which length is greater than 5 
print(a)

c=[1,2,3,13,17,25,37,46,22,33,44]
d =["even" if i%2==0 else "odd" for i in c]
print(d)

e = ["rohit","anmol","fouji","manna"]
f =[i.upper() for i in e]
print(f)

# # # #1. Create a list of square of the list of number[6,9,10,12,25]
g = [6,9,10,12,25]
h = [i**2 for i in g]
print(h)

#2 
j = [1,2,3,4,5]
k = [i if i%2==0 else i*10 for i in j]
print(k)

# # # ##SETS 
# 1. mutable data type
# # 2. stores a value in unordered format 
# 3.dont store duplicate value 
# 4.sets are stored in{}braces
# 5. stored hetrogeneous data

a={}#gives dict not for crate empty sset 
print(type(a))

s=set()# use for create empty set
print(type(s))

d = {1,2,3,4,5}
print(d)
e={1,"hello",25,26,26.8,"hello"}
print(e)

# # #adding a element in set 
# .add()#add only one element 
# .update([])#add full list but not existing element 
s = {"hello",1,5,4,92}
print(s)
s.add(22)#adding element
print(s)
s.update([1,2,3,4,5])
print("AFTER UPDATE")
print(s)

# # #traversing in set
# for i in s:
#    print(i,end=" ")


#removing element form set
# 1.pop() remove the first element 
# 2. remove() removing the given value 
# 3. delete() 
x = {2,98,56,"hii",27}
x.pop()#removing the first element 
print(x)

x.remove(98)#removing the given value 
print(x)

# x.remove(6)#crestes error when element not in set 
# print(x)
x.discard(6)#it not create error when element not in set python know 6 not in set they not create error 
x.discard(56)#simply remove 5
print(x)


# # #frozen sets 
# a=frozenset([1,2,3,4,5])#set can be immutable and not give any output 
# print(a)
# a.add(8)

a= {1,2,3,4,5}
b= {4,5,6,7,8}

# # #union,intersection,difference,symmetric difference,subsets
# # print(a|b)
# # print(a.union(b))#union
# # print(a&b)
# # print(a.intersection(b))#intersection
# # print(a-b)
# # print(a.difference(b))#difference
# # print(a^b)#symmetric difference
# # # print(a.symmetric)

# # d={5,6,7}
# # print(d.issubset(b))
# # print(d.issuperset(b))
# # print(d.isdisjoint(b))