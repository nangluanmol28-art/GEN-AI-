print("hello")
# #for run python file on the other computer write puthon file name in terminal and press enter 
#data types 
#string  "hello", 'anmol' 
#int  1,2,3,4,-4,-4
#float   0.5,0.6,0.8,3.0,10.65
#boolean - true or false explain and fix problems 
# ctrl / for comments 

# #variables assning a value to variables 
# # value is literatel 
a = 20 
print(a)
print(type(a))
b = 0.5
c = "python"
d = True 
print(type(b))
print(type(c))
print(type(d))

print("anmol",end="")#end is used to print next line in same line 
print("hello")
#\n = new line 
#\t = tab space proper amount of space 
price = 50 
price1 = 250 
price2 = 120 
print("1. burger \t- 50 \n2. Pizza \t- 250 \n3. Pasta \t- 120")
print("1. burger \t-",price,"\n2. Pizza \t-",price1,"\n3. Pasta \t-",price2)

# # take input from user 
ab = input("enter your name: ")
print(ab)
print(type(ab))

# #numeric value 
e = int(input("enter your age:"))
print(e)

#type casting 
f = 10 
f = str(f)
print(type(f))

#operators 

#arithmetic operators (+,-,*,/,%.//,**)
#** power ,// floor devision quotient , % reminder 
a = 100
b = 20 

print("sum = ",a+b )
print("difference = ",a-b)
print("product =",a*b)
print("division =",a/b)
print("floor division =",a/b)
print("power =",a**b)
print("modulus =",a%b)



#logical (and,or,not)
#and - both condition should be true 
#or - any one should be true 
#not - gives opposite answer false to true true to false 

age = 20
salary = 30000
print(age>18 and salary>25000)   #true 

age = 20
salary = 20000
print(age>18 or salary>25000)   #true one is true 

age = 16
print(not(age>18))              #true 

#assignment operators (=,+=,-=,*=,/=,%=,**=,//=)
a = 10
b=10
c=10
d=10
#a = a+5 or a+=5 
#a = a-5 or a-=5 
#a = a*5 or a*=5
a+=5
b-=5
c*=5
d/=5
print(a)
print(b)
print(c)
print(d)

#comparison operators (==,!=,>,<,>=,<=)  gives boolean value 
#== checks equality
#!= checks not equal
#> checks greater than
#< checks less than
a=10 
print(a==10)
print(a!=10)
print(a>10)
print(a<10)
print(a>=10)
print(a<=10)



# c = 20 
# d = 30 
# e = 25 
# f = 15 
# print(c==d)
# print(c!=d)


#membership operators (in,not in)   true false answer 
#in checks if a value is present in a sequence (like list, string, tuple)
s1 = "i am playing cricket"
print("anmol"in s1)
print("cricket" in s1 )
print("football" not in s1)

#indentity operators (is, is not)
#is checks if two variables point to the same object in memory
a = [1, 2, 3]
b = a

print(a is b)   #true 

a = [1, 2, 3]
b = 10

print(a is not b)  # true


#if elif else

age = int(input("enter your age:"))
if age >=18:
      print("you are eligible to vote")
else:
      print("you are not eligible to vote")

marks = int(input("enter your marks:"))

if marks>=90 and marks<=100:
      print("grade A")
elif marks>=80 and marks<=89:
      print("grade B")
elif marks>=70 and marks<=79:
      print("grade C")
elif marks<=69 and marks>=0:
      print("fail")
else:
      print("invalid input")


#odd even 
num = int(input("Enter a number:"))
if num%2 == 0:
      print("even")
else:
      print("odd")

#for loop
for i in range(10):
      print(i)

for i in range(10):
      print("hello")

for i in range(1,20):#print numbers from 1 to 19
        print(i)

for k in range(2,50,3):#to every 3rd number from 2 to 50
      print(k)
for l in range(50,2,-2):#to backward even  numbers from 50 to 2
        print(l)



subjects = int(input("Enter number of subjects:"))#for the marks of more than one subject we use loop to take input and print grade for each subject
for i in range(subjects):
      marks = int(input("enter your marks:"))

      if marks>=90 and marks<=100:
            print("grade A")
      elif marks>=80 and marks<=89:
            print("grade b")
      elif marks>=70 and marks<=79:
            print("grade c")
      elif marks<=69 and marks>=0:
            print("fail")
      else:
            print("invalid input ")
