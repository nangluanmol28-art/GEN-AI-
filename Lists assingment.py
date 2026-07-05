travelbag =["passport",3,"charger",120.50,"sunglasses",'True']
#1
print(travelbag)
#2
print(travelbag[0])
print(travelbag[5])
#3
print(travelbag[-2])
#4
print(travelbag[2:4])
#5
print(travelbag[::-1])

#Q2\
scores=[85,92,78,92,89,76]
#1.
scores.extend([95,88,82])
print(scores)
#2.
scores.append([5,10])
print(scores)
#3.
print(scores[9])
print(scores[9][1])
#4
scores.insert(3,90)
print(scores)
#5
scores.pop()
print(scores)
#6
scores.pop(5)
print(scores)
#7
scores.remove(92)
print(scores)
#8
print(scores.count(92))
#9
scores.sort(reverse=True)
print(scores)
#10
scores.reverse()
print(scores)

print("==========PART 3==========")
classroom=[
    ["Alice",90,80],
    ["Bob",78,82],
    ["Charlie",95,91],
    ["Diana",85,89],
]
print("Charlies Science Grade:", classroom[2][2])
print("Bob's Math Grade:", classroom[1][1])
classroom[3][1] = 88 #updated classroom using indexing 
print("Updated Classroom:",classroom)

print("=====Students Average Marks=====")
for student in classroom:
    name = student[0]
    average = (student[1]+student[2])/2
    print(name,"Average marks",average)

print("=====PART 4=====")
multiples_of_three = []

for i in range(1,31):
    if i%3==0 :
        multiples_of_three.append(i)
print("Multiples of 3:",multiples_of_three)

for i in range(len(multiples_of_three)):
    print("Index",i ,"contains",multiples_of_three[i])

print("=====PART 5=====")
products = ["Laptop", "Smartphone", "Headphones", "Tablet"]
prices = [1200, 800, 150, 450]

print("Product List:")
for product, price in zip(products,prices):
    print("Product:",product,"|Prices :$",price)
#part 2 pending 




#Q3 
day_1_sales = [10, 15, 8, 12]
day_2_sales = [5, 20, 12, 18]
for i,j,k in zip(products,day_1_sales,day_2_sales):
    total_sales = j+k
    print("product:",i,"|Total Sales:",total_sales)

