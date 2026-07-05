# # # #Easy practice problems

# # # # print("Area Calculator")
# # # # l = int(input("Enter the Length of the Rectangle: "))
# # # # b = int(input("Enter the breadth of the Rectangle: "))
# # # # print("Area of The Rectangle =",l*b)


# # # # print("Multiples of the 5 or not")
# # # # n = int(input("Enter a Number: "))
# # # # if n%5  == 0:
# # # #     print("Given No. is the multiple of the 5")
# # # # else:
# # # #     print("Given No. is not the multiple of 5")


# # # # print("Checking For The Driving Eligibility")
# # # # age = int(input("Enter your age="))
# # # # if age>18:
# # # #     print("You Are Eligible to Drive")
# # # # else:
# # # #     print("Your Are Not Eligible To Drive")



# # # # print("python 7 times using for loop")
# # # # for i in  range(7):
# # # #     print("python")


# # # # print("Variable Swapping")
# # # # x= 10
# # # # y = 25

# # # # x,y = y,x
# # # # print("x=",x)
# # # # print("y=",y)


# # # #medium practice problems 
# # # print("==========Simple Calculator==========")
# # # a = int(input("Enter a first no.="))
# # # b = int(input("Enter a second No.="))
# # # op = input("Enter a operator(+,-,*,/):")
# # # if op=="+":
# # #     print("Result:",a+b)
# # # elif op=="-":
# # #     print("Result:",a-b)
# # # elif op=="*":
# # #     print("result:",a*b)
# # # elif op=="/":
# # #     if b!=0:
# # #         print("Result:",a/b)
# # #     else:
# # #         print("Division by 0 is not allowed")
# # # else:
# # #     print("invalid operator")        


# # print("Checking for the leap year ")
# # year = int(input("Enter a year :"))
# # if year%400==0:
# #     print(year,"is a Leap year")
# # elif year % 4 == 0 and year % 100 != 0:
# #     print(year,"is a leap year")
# # else:
# #     print(year,"is not a leap year")

# #FizzBuzz 
# # for i in range(1,21):
# #     if i%3 ==0 and i%5==0:
# #         print("Fizz Buzz")
# #     elif i%3==0:
# #         print("Fizz")
# #     elif i%5==0: 
# #         print("Buzz")
# #     else:
# #         print(i)


# ###Factorial 
# # a = int(input("Enter a number:"))
# # b =1
# # for i in range(1,a+1):
# #     b = b*i
# # print("Fictorial of",a,"is",b)

# a = int(input("Enter The Purchase Amount:"))
# if a>100:
#     print("discount=0.10")
#     print("Final Amount=",a-0.10)

# elif a>500:
#     print("Discount=0.20")
#     print("Final Amount=",a-0.20)
# else:
#     print("No Discount")
#     print("Final Amount",a)

#Advanced practice Problems 
# The Fibonacci sequence is a series of numbers where each number is the sum of the previous two.
# f = int(input("Enter a number For fibonacci sequence:"))
# a=0
# b=1
# for i in range(f):
#     print(a)
#     a,b=b,a+b


#number guessing game 
# h = 42
# for attempts in range(1,6):
#     guess = int(input("Enter Your Guess:"))
#     if guess==h:
#         print("Congratulation Your Guessing number is correct")
#         break
#     elif guess>h:
#         print("Too High!")
#     else:
#         print("Too Low!")
# else:
#         print("Your are a ran of the attempts")
#         print("The Hidden No. is",h)


s = input("Enter a Word:")

