print("==========Question 1 ==========")

my_list = [10, 20, 20, 30, 40, 40, 50]
unique_numbers = set(my_list)
print("UNIQUE NUMBERS:",unique_numbers)

even_numbers = {20,40,60,80}
print("INTERSECTION OF BOTH:",unique_numbers.intersection(even_numbers))

print("UNION OF BOTH:",unique_numbers|even_numbers)#union

print("\n==========Question 2 ==========\n")
my_set =set()
my_set.add(5)
my_set.add(10)
my_set.update([15,20,25])
my_set.remove(10)
print("FINAL SET:",my_set)
print("IS SUBSET",my_set.issubset({5,15,20,25,30}))

print("\n==========Question 3 ==========\n")

student_info = ("Alice",20,"A")
name , age ,grade = student_info
print("NAME:",name)
print("AGE:",age)
print("GRADE:",grade)

# student_info[0] ="Bob"  # This will cause an error since tuples are immutable
# print(student_info)


print("\n==========Question 4 ==========\n")
scores = (85, 90, 85, 70, 85, 95)
print("Count of 85 :",scores.count(85))
print("First Index of 90:",scores.index(90))

print("\n==========Question 5 ==========\n")
employee = {'name' : 'Anmol', 'department':'CSE AI ML ','salary': 60000}
employee.update({'salary':70000})
print("\nUpdated Salary:",employee)
employee.update({"role":"Manager"})
print("\nUpdated Employee Info:",employee)
employee.pop('department')
print("\nAfter Removing Department:",employee)


print("\n==========Question 6 ==========\n")
capitals = {"France": "Paris", "Japan": "Tokyo", "India": "New Delhi"}
print("Countries: ", end = " ")
for i in capitals.keys():
    print(i, end = ", ")
 # Print a newline

print("\nCapitals:",end = " ")
for i in capitals.values():
    print(i, end=",")

for i in capitals.items():
    print("\nThe Capital of ",i[0],"is",i[1])

print("\n==========Question 7 ==========\n")
nums = [1,2,3,4,5]
squares_dict = {i: i**2 for i in nums}
print(squares_dict)

print("\n==========Question 8 ==========\n")
marks = {"Alice": 85, "Bob": 40, "Charlie": 92, "David": 55}
passed_students ={i:marks[i] for i in marks if marks[i] >= 60}
print(passed_students)

print("\n==========Question 9 ==========\n")
def greet(name):
    return "Good Morning," + name

message = greet("Anmol")
print(message)

def generate_table(n):
    table = []
    for i in range(1,11):
        table.append(n*i)
    return table 
table = generate_table(13)
print("Table of 13:",table)

print("\n==========Question 10 ==========\n")
def check_prime(n):
    if n <= 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True 
print("Is 47 prime?",check_prime(47))

def remove_duplicates_and_sort(lst):
    cleaned = list(set(lst))
    cleaned .sort()
    return cleaned 
lst = [1,1,1,2,2,4,5,6,8,8,6]
print("Cleaned List:",remove_duplicates_and_sort(lst))




