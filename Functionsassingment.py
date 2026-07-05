print("========== Part 1 ==========")



def multiply_numbers(a,b=10):
    return a*b
print(multiply_numbers(5,4))
print(multiply_numbers(7))

def sum_all(*arg):
    sum = 0
    for i in arg:
        sum+=i
    return sum 
print("Sum all(1,2,3):",sum_all(1,2,3))
print("Sum all(10,20,30,40):",sum_all(10,20,30,40))


def top_student(**kwargs):
    highest_score =0
    topper = ""
    for i,j in kwargs.items():
        if j>highest_score:
            highest_score = j
            topper = i
    return topper
a = top_student(alice=85, bob=92, charlie=78)
print("Top Student:",a)

print("\n========== Part 2 ==========")
u = lambda text:text.upper()
print("Uppercase String:",u("hello world"))

print("\n========== Part 3 ==========")
mixed_list = [1, "hello", 3.14, "world", 42]
x = filter(lambda a:isinstance())