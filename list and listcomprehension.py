print("\n========== Part 1 ==========\n")
fruits=["apple",'banana','strawberry','orange','grapes','litchi']
fruits[2]="Mango"
print("Updated List:",fruits)
print("First 3 Letters:", fruits[:3])
print("Last 2 Letters:",fruits[-2:])
print("Reverse List:",fruits[::-1])


print("\n========== Part 2 ==========\n")
numbers = [2, 5, 8, 11, 14, 17, 20, 25]
a = [i**2 for i in numbers]
print("Squares:",a)
even = [i for i in numbers if i%2==0]
print("Even Values:",even)


print("\n========== Part 3 ==========\n")#if else logic 
temps = [35, 12, 40, 8, 22, 45, 18]
weather=["Hot" if i>30 else "Cool" for i in temps]
print("Weather:",weather)

print("\n==========Part 4 ==========\n")#string manipulation 
names = ['alice', 'bob', 'charlie', 'diana', 'edward']
a = [i.upper() for i in names]
print("Capitalized Names:",a)
b=[i for i in names if len(i)>=5]
print(b)

print("\n========== Part 5 ==========\n")
my_list = []
my_list.append(10)
my_list.append(20)
my_list.append(30)
# print(my_list)
my_list.insert(1,15)
# print(my_list)
my_list.remove(20)
# print(my_list)
my_list.pop()
# print(my_list)

unorded = [8,3,1,5,4]
unorded.sort()
print(my_list)
print(unorded)


print("\n========== Part 6 ==========\n")
words = ["python", "data", "science", "machine", "learning"]
word_lengths = [ len(i) for i in words  ]
print("Length of Words:",word_lengths)

prices = [100, 250, 45, 300, 80]
a = [price*0.9 if price>150 else price for price in prices]
print("Discounted Prices:",a)