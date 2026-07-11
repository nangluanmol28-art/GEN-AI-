# f strings 
name = "alice" 
age = 25
greeting = f"Hello, my name is {name} and i am {age} years old "
print(greeting)


# math and expression in sf string 
num1 = 10
num2 = 5 
print(f"If you add{num1 }and num{2},you get{num1 + num2 }")
# print(f"")

# with deciomals

price = 49.9
tax  = 0.075
total = price + (price*tax)
print(f"Raw total:{total}")
print(f"formated total(2decimals): ${total:.2f}")

# formating large numbers with commas 
large_number = 1000000
print(f"Large numbers {large_number:,}")
# print("large numbers:", large_number.split[3:,])
print(f""" 
===========
Anmol Singh
===========          

""")