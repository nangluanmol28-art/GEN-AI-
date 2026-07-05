#if statement nested in if 
marks = int(input("Enter Your marks:"))
if marks>=90 and marks<=100:
    if marks>=95 and marks<=100:
     print("grade A+")
else:
    print("grade A")

#nested loop
#for nested in for 
for i in range(1,11):#printrows
   for j in range(i):#printcoloumn 
      print("*",end ="")
   print()   


for i in range(1,6):
 for j in range(0,i):
        print("*", end = " ")
        print()
for i in range(10):#printrows
   for j in range(10,i,-1):#printcoloumn 
      print("*",end ="")
   print()     

#strings
s="anmol"
print("s")

print(len(s))   #lenght function 

s1="mandeep kaur"  #including space
print(len(s1))

#slicing 

print(s1[0])# 1 m 
print(s1[0:7])#0 to 6
print(s1[:])#full 
print(s1[7:0:-1])
print(s1[1:8:2])

#methods 
print(s1.lower())#lower
print(s1.upper())#capital
print(s1.title())# first letter capital 
print(s1.capitalize())#only first letter of full line or paragraph 4
print(s1.swapcase())#smaal big big small
print(s1.startswith("ma"))#check the first letter boolean value
print(s1.endswith("kaur"))


#striping 

c ="         hello      hi   "
print(c)
print(c.strip())#remove space from both side 
print(c.rstrip())#remove right space 
print(c.lstrip())#remove left space 


#replace 

d = "how are you "
# d= d.replace("o","i")
# print(d)

d = d.replace("how","where")
print(d)


#splitting 

e="what is this "
print(d.split(" "))# give all words in list when give space 
print(e.split("h"))#

f="cjdciidwwisjw#sswjid#hbwdjw#"#split from the #
print(f.split("#"))