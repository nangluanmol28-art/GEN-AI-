#lists(mutuable,ordered,indexed,hetrogeneous)

li = [10,20,30,"apple",40.5,True]#print in the lists
print(li)

# #slicing know the element at position
print(li[4])
print(li[0:3])
print(li[3:5])
print(li[::-1])#print reverse 
print(li[-1])#for printing the last index 


# #adding elements 
# .extend([]) - adding multiple element in list
# .append([]) - adding full list or only one element in list 
# .insert() - adding element in given place
li1 = [30,50,60,20,70,100]
li1.extend([99,10000])#adding one elements in list
print(li1)

li1.append([20,30,40])#adding full list 
li1.append(900)
print(li1)

print(li1[8])#for accessing the lsit in list 
print(li1[8][1])#for accessing the particular element of the list 

li1.insert(5,650)#for adding the index in the given place 
print(li1)

li1.insert(4,[12,13,14])
print(li1)

#removing elements 
# .pop - default to print list
# .pop(3) - remove the given place value 
# .remove - remove the given value only one time 
#
li2 = [20,30,40,20,70,90]
li2.pop#default parameter-1
print(li2)
li2.pop(3)#remove the given place value
print(li2)

li2.remove(20)#remove only one time not if value is repeated 
print(li2)



#LIST MANUPILATION
# .sort() - assending 
# .sort(reverse = True) - desending 
# .reverse() - for reverse the string 
# 
li2.sort()#assending 
print(li2)

li2.sort(reverse = True)#desending 
print(li2)

li2.reverse()#for reverse the string 
print(li2)

#count
print(li2.count(40))# calculate the number of value present 

# creating a list using loop 
l= []
for i in range(1,20):#for acsseing the full list
    l.append(i)
print(l)

for i in l:#acsessing the elements or transversing
    print(i)

# #zip function
a = [1,2,3,4]
b = ["a","b","c","d"]
for i in zip(a,b):#for combine the list a and b in list form
    print(i)

for i,j in zip(a,b):# for acssesing the simple combine not in the list 
    print(i,"-",j)

# #join only works in the string give error in the integer 
l3 = ["hello","how","are","you"]#combine the list to make sentence 
print("_".join(l3))
