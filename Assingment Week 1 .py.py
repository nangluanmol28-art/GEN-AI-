# print("Assingment Week 1 'The Cafe Ordering System' ")

#part 1 welcome message 
print("========== Welcome To The Nanglu Cafe ==========")

name = input("\nEnter Your Full Name: ") #get the name of coustmer 
age = int(input("\nEnter Your Age: "))  #for the discount 
name = name.strip().title() #strip use to remove extra space and title use to capitalized the first letter 
firstname = name.split()[0]   #extract only first name and make a new variable 
print("\nHello,",firstname)

#part 2 menu 

menu = "Burger ,Pasta ,Pizza ,Coffee "
print("\nAvaliable Menu:",menu)

order = input("\nWhat you Want To Order? = ").title()#ask coustmer what they want to order and title is used to capitalized the first letter 
#print("order", in menu)

#membership operator 
menu = "Burger ,Pasta ,Pizza ,Coffee "

if order not in menu:
    print("\nsorry! Sir This item not avaliable in our menu. ")
else:
    quantity = int(input("Enter quantity:"))
    price = 150
    totalcost = price*quantity

    print("Initial Bill Amount: ",totalcost)

#discounts and logics 

if age<18 or quantity>=5:
    discount = totalcost * 0.1
    print("\nYou got a 10% Discount")
elif age>60:
    discount = totalcost * 0.2
    print("\nYou got a 20% Discount ")
else:
    discount = 0
    print("\nNo Discount Is Applied")

finalbill = totalcost-discount
print("Final Bill is :",finalbill)
#recipt and nested logic 

if finalbill>500:
    if name[0].upper() == "A" or name[0].upper() == "S":
        print("****** VIP COUSTMER ******")

for i in range(2):
    for j in range(10):
        print("*",end=" ")
    print()

print("Full Name:",name)
print("Item Ordered:",order)
print("Quantity",quantity)
print("Final Bill:",finalbill)

for i in range(2):
    for j in range(10):
        print("*",end=" ")
    print()