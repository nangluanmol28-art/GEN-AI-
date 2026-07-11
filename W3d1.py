# OOPs - object oriented programming 
# using the self to stores the value dont need to give parameters when call the function
class dog:
    def __init__(self,name,age,breed):
        self.name = name
        self.age = age 
        self.breed = breed 
    def bark(self):
        print(f"{self.name} says hooh!")

    def info(self):
        print(f"Name is : {self.name} and Age is: {self.age}")

    # updating values 
    def birthday(self):
        self.age += 1 
        print(f"You are {self.age} years old")
    
dog1 = dog("Golu",3,"Paperian")
dog2 = dog("Jackey",5,"Desikutta")
print(dog1.name,dog2.name)
print(dog1.age,dog2.age)
print(dog1.breed,dog2.breed)

# method calling 
dog1.bark()
dog2.bark()
dog1.info()
dog2.info()
dog1.birthday()
dog2.birthday()

# Example of making the bank acoount where we can seee the 

class BankAccount:
    def __init__(self,owner_name,initial_balance=0.0):
        self.owner = owner_name
        self.balance = initial_balance
        print(f"{self.owner} Your Bank account is successfully created and initial balance is  {self.balance}")
    # we can also keep a transiction history as a list
        self.transiction_history = []
        self.transiction_history.append(f"Account opened with ${self.balance}")
    # Add deposite function
    def deposit(self,amount):
        if amount>0:
            self.balance += amount
            self.transiction_history.append(f"Credit: +${amount:.2f}")
            print(f"Success:${amount:.2f} deposited into {self.owner} account.")
        else:
            print(f"Error: Deposited amount must be positive.")

    def withdraw(self,amount):
        if amount <=0:
            print("Error: Withdrawal amount should be positive ")

        if amount > self.balance:
            print(f"Error: Insufficient balance You have only ${self.balance:.2f}")
        else:
            self.balance -= amount
            self.transiction_history.append(f"Debit: -${amount:.2f}")
            print(f"Successfully ${amount:.2f} withdrawn from {self.owner} account.")

    def show_balance(self):
        print(f"---{self.owner} account Balance: ${self.balance:.2f}---")

    def print_statement(self):
        print(f"\n==========BANK STATEMENT FOR {self.owner.upper()}==========")
        for transictions in self.transiction_history:
            print(transictions)
            print(f"Final Balanace: ${self.balance:.2f}")
        print(f"\n==========END OF THE SCRIPT============\n")
print(f"""==================================================\n""")            


# print(f"1. creating account")
b_account = BankAccount("Anmol Singh",50000.0)

# print(f" 2. making transactions ")
b_account.deposit(4000.0)
b_account.withdraw(10000.0)
b_account.withdraw(100000.0)#fail because insufficient balance 

# print(f"\n3.show individual balance ")
b_account.show_balance()

# print(f"\n 4. Print statements")
b_account.print_statement()



