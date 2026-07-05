#dict_comprehension
#expression
#{key:value for item in iterable}

#weite a program to create a dictoniary as numbers its keys and its squares as its values upto 10 numbers only 
d={}#in the for loop
for i in range(1,11):#in list comprehensen
    d[i]=i**2
print(d)

#in dictcomprehension
d1={i:i**2 for i in range(1,11)}
print(d1)

# make a dictoniary 
names=['neha','Karan','Nirika']
e = {i:len(i) for i in names} 
print(e)

f={i:"even" if i%2==0 else "odd" for i in range(1,11)}
print(f)

students={'Sumit':80,'Jatin':40,'Harman':40,'Gurjot':90}
g = {i:"Pass" if students[i]>50 else "fail" for i in students}
print(g)

o={1:'odd',2:'Even'}
reverse={v:k for k,v in o.items()}
print(reverse)


##Functions 
#built in functions 
#enumerate(),zip(),map(),filter(),


#user defined function 
#that are defined by the user for specific functions 

#USER DEFINED FUNCTION
#syntax
# def function_name(parameters):
     #statement--1
     #statement -- n
     

     #return value()
#normal function
def greet():
    print("Hello")

greet()
greet()
greet()
greet()
# function with parameters 
def greet(name):
    print("Hello",name)
greet("Anmol")
def greet():
    # print("Good morning")
    return "Good morning!!"
    
a=greet()
print(a,"anmol")

def add(a,b):

    return a+b
print(add(10,20))

# #input from user
def add():
    x=int(input("Enter number 1:"))
    y=int(input("Enter number 2 :"))
    return x+y
result=add()
print("sum=",result)

# #positional arguments 
def multi(a,b,c):
    return a*b*c

print(multi(2,3,4))

# #keyword arguments 
def sub(a,b,c):
    print(a-b-c)
sub(a=10,c=50,b=200)

# #default parameter 
def summ(a,b,c=3):
    return a+b+c
print(summ(10,20))



def table(n):
    for i in range(1,11):
        print ( n, "x", i ,"=", n*i)
table(13)



#function to check number is prime or odd 
def check_prime(n):
    count = 0
    for i in range(2,n):
        if(n%i==0):
            count=1
            break
    if count==0:
        return"The number is prime"
    else:
        return"The number is not prime"
a=check_prime(47)
print(a)


a=[1,1,1,2,2,4,5,6,8,8,6]
# #make a function to give list that not contain duplicate value
def remove_duplicates(a):
    a.sort()
    i=0
    while(i<len(a)):
        if(a[i]==a[i-1]):
            del a[i-1]    
print(remove_duplicates(a))



