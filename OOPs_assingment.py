class student():
    # Part 1 (definea class and __init__)
    def __init__(self,name,grade_level,score):
        self.name = name 
        self.grade_level = grade_level
        self.score = score 
        print(f"{self.name} has a score of {self.score}")
    #part 3
    def introduce(self):
        print(f"Hii , My name is {self.name} and I am in the {self.grade_level}")

    #part 4
    def improve_score(self,extra_points):
        self.score += extra_points
        print(f"{self.name} score has improved to {self.score}.")

print(f"""==========Part 2 (Creating objects and accessing attributes )==========""")
student1 = student("Anmol Singh", "10th",94)
student2 = student("Rohit Singh","11th",95)

# print(student1.name)

print(f"""========== Part 3 (adding and calling methods) ==========""")
student1.introduce()
student2.introduce()
# calling 
student1.improve_score(1)
# verify the score changed 
print(f"Final check - {student1.name}'s score is : {student1.score}")