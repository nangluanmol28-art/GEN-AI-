import sys
import os 
import datetime
import math 

print("========== 1. Sys Module ==========")
# sys.argv - Stores the argument 
# sys.platform - Tells the operating system
# sys.version - shows python version 
# sys.getsizeof() - Return memory size of an object 
# 
# The sys module provides access to some variables used or maintained by the
# interpreter and to functions that interact strongly with the interpreter.
print("sys.argv( Argumrnts passed to script)):",sys.argv)
print("Operating System is :",sys.platform)
print("Version of system :",sys.version)
num = 42 
print("Integer (42):",sys.getsizeof(num),"bytes")
text = "Hello , World!"
print("String (Hello,World!):",sys.getsizeof(text),"bytes")
list = [1,2,3,4,5,6]
print("list = [1,2,3,4,5,6]:",sys.getsizeof(list),"bytes")
tuple = (1,2,3,4,5)
print("tuple = (1,2,3,4,5):",sys.getsizeof(tuple),"bytes")

print("\n========== 2. The OS Module ==========")
#It helps you work with files, folders, directories, environment variables, and execute OS-related tasks.
#os.getcwd() -  get current working directory
#os.chdir() - change directory
#os.listdir() - List files and folders
#os.mkdir() - create one folder 
#os.makedirs() - create multiple folder 
#os.rmdir() - remove an empty folder 
#os.remove - delete a file  
#os.rename() - rename a folder 
# os.path.exists()- check if a file or folder exist 
cwd = os.getcwd()

print("My Directory name:",cwd)
# cwd = os.getcwd()
print(cwd)

print(os.listdir())
dirs = os.listdir()#for list the files 
for i in range(3):
    print(dirs[i])

# path1 = os.path.join(cwd,"new_folder","new.txt")
# print(path1)

#makedir ,rmdir
# path1 = "demo folder"
# if os.path.exists(path1):
#     print("Folder exists:",path1)
#     os.rmdir(path1)
#     print("Removing Path")

# else:
#     print("Folder does not exist:",path1)
#     print("creating path.....")
#     os.makedirs(path1)
#     print("Path created successfully...")
# print(os.name)

print("========== 3. DateTime Module ==========")
#use for working with date and time 
#  Get the current date
#  Get the current time
#  Create custom dates
#  Add or subtract days
#  Format dates and times
#  Calculate the difference between dates

# 3.1 getting current date and time 
now = datetime.datetime.now()
print("Current date and time :",now )

# 3.2 date objects (year,month,day)
today = datetime.date.today()
print(today)
print("year:",today.year,"month:",today.month,"Day:",today.day)

s="26-07-04"
print(s.split("-"))

specific_datetime = datetime.datetime(2025,12,25,18,30,0)
print("Specific Date/Time:",specific_datetime)

print("\n========== 4. The Math Module ==========")
# The math module provides access to mathematical functions defined by the C standard.
# 1. constants
# 2. numeric representations 
# 3. operations 
# 4. power and logathrimatric 
# 5. trignometry and angle 

# 4.1
print("Math constants:")
print("Pi",math.pi)
print("Euler numer",math.e)
print("tau",math.tau)

# 4.2
print("\n Rounding and absolute value :")
value = -5.67
print("Original valuen :",value)
print("smallest integer >= value:",math.ceil(value))
# print("largest integer <= value:",math.floor(value))
print(f"  math.trunc({value}) (Truncates decimal part):", math.trunc(value))
print(f"  math.floor({value}) (Largest integer <= val):", math.floor(value))

# 4.3 operations
print("\n Mathematical operations:")
print("Factorial:",math.factorial(7))
print("Greater common divisor:",math.gcd(24,36))

# 4.4 power and logarithmic 
print("\n Power and logamithmic function:")
print("Square Root :",math.sqrt(64))
print("2 di power  5: ",math.pow(2,5))

# 4.5 trigonometry and angle conversion 
print("\n Trigonometry:")
# angle = 45 
angle_deg = 45
angle_rad = math.radians(angle_deg)

print("Converting", angle_deg, "degrees to radians:", angle_rad, "radians")
print("Sine of 45 degrees:", math.sin(angle_rad))
print("Cosine of 45 degrees:", math.cos(angle_rad))
print("Converting", angle_rad, "radians back to degrees:", math.degrees(angle_rad), "degrees")

