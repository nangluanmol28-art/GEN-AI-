# file Handling
print("========== File handling ==========")
#  Common File Handling Modes:
# 'r'  - Read (Default): Opens a file for reading, errors if the file doesn't exist.
# 'w'  - Write: Opens a file for writing, creates the file if it does not exist or truncates the file if it exists.
# 'a'  - Append: Opens a file for appending, creates the file if it does not exist.
# 'x'  - Create: Creates the specified file, returns an error if the file exists.
# 't'  - Text (Default): Text mode.
# 'b'  - Binary: Binary mode (e.g. images).
# '+'  - Read/Write: Opens a file for updating (reading and writing).

# Writing to a file using 'w' mode (this creates the file or overwrites it)
# # We use the 'with' statement so the file automatically closes after we're done.
with open("demo.txt","w") as file:
    file.write("Sanam ")
    file.write("\nKrish")
    file.write("\nPooja")
print("writing is done")

with open ("student.txt","w") as file :
    file.write("Alice\n")
    file.write("bob\n")
    file.write("pooja")
print("Successfully wrote to 'student.txt',")

# # Reading from a file using 'r' mode
print("\nReading contents of 'demo.txt':")
with open("demo.txt", "r") as file:
    contents = file.read()
    print(contents)

# # Appending to a file using 'a' mode (adds to the end without overwriting)
with open("demo.txt","a") as file:
    file.write("\nBalwinder\n")
print("Appened new content to file......... ")

# Over writing demo.txt  python delete the first content from the file and write this content 
with open("demo.txt","w") as file:
    file.write("\nVansh ")
    file.write("\nAnmol")
    file.write("\nVishal")
print("Overwrite on the file using the w ")

# for reading the file     
with open("student.txt","r") as file:
    contents = file.read()
    print(contents)

# Reading Line by Line(Useful for large files )
# for loop uses not a particular function 

print("\nRead Line by Line:")
with open("demo.txt","r") as file:
    for line in file :
        print("student: {}".format(line.strip()))#.strip removes the new line characters 

# Reading all lines into a list using 
# readlines()
print("\nReading all lines into a list:")
with open("demo.txt","r") as file:
    line_list = file.readlines()
    print("List of Lines:",line_list)
    print("Total students:",len(line_list))

# write multiple lines using writelines()
# uses to write multiple lines easy 
print("\n Writing Multiple lines at once")
new_students = ["avneet\n","Karan\n","Rohit\n"]
with open("demo.txt","w") as file:
    file.writelines(new_students)
print("Successfully wrote new_students to demo.txt")


# checking if file exist before reading
import os 
print("\n Checlking if a file exists:")
if os.path.exists("demo.txt"):
    print("'demo.txt' exist. we can safely read it ")
else:
    print("'demo.txt path dont exist.'")

# FILE EXCEPTING 
print("========== 2. File Excepting ==========")

# with open ("missing_file.txt","r") as file:
#     data = file.read()
# This gives the error if file does not exist so we do exceotion handling 
# names of error
# FileNotFoundError
# ZeroDivisionError
# ValueError
# IndexError
# KeyError
# Generic exception  

try:
    with open("MISSING.txt","r") as file:
        data = file.read()
except FileNotFoundError:
    print("Error: The File 'MISSING.txt' not found" )

# Handling multiple exceptions and using 'else' and 'finally'

print("\nDividing numbers:")
try:
    num1 = 10
    num2 = int(input("Enter a number to divide by(try 0 to see the error):"))
    result = num1/num2
except ZeroDivisionError:
    print("Error: Cannot divide by zero ")
except ValueError:
    print("Error: Invalid Output please enter an integer")
else:#this exception only if no exception occured 
    print("The result is ",result)
finally:#This runs Always, no matter what happen (good for cleanup)
    print("Execution of the divisor try/except block is complete.")
    
# Catching Index Error (List out of bounds )
print("\nAccessing Lists ")
my_list = [1,2,3]
try:
    print("Trying to access index 5...")
    value = my_list[5]
except IndexError:
    print("Error: Index out of range The list not have that elements.")
else:
    print(value)

# CAtching Key Error (Dictoniary Key missing)
print("\n Accessing Dictoniary")
my_dict = {"name":"Anmol","Course":"Python"}
try:
    print("Trying to access 'city'...")
    city = my_dict["city"]
except KeyError:
    print("Error: Key not in the dictoniary ")

# Catching The generic Exception (Catch-all)
print("\n Generic Catch-all")
try:# A generic error,for example a type error
    result = "10"+5
except Exception as e:
    print(e)



