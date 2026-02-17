class Student:
    def __init__(self):
        self.name = input("Enter your Name ")
        self.roll_no = int(input("Enter your Roll No "))
        self.marks = float(input("Enter your Marks "))

    def update_marks(self):
        self.marks = float(input("Enter New Marks"))
        print(f"New Marks {self.marks}")    
        return self.marks

    def display_info(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Marks:", self.marks)
        print("---------------------")

    def chk_res(self):
        if self.marks >40:
            print("Student  Passed")
        else:
            print("Student Failed")
    def asg_grd(self):
        if self.marks>=85:
            print("Grade A")
        elif self.marks>=70 and self.marks<85:
            print("Grade B")
        elif self.marks>=55 and self.marks<70:
            print("Grade C")
        elif self.marks>=40 and self.marks<55:
            print("Grade D")
        elif self.marks<40:
            print("Grade F")

# Creating Student objects
student1 = Student()
student2 = Student()

# Calling display_info() method
student1.display_info()
student1.asg_grd()
student1.chk_res()
student1.display_info()
student2.display_info()
student2.asg_grd()
student2.chk_res()
student2.display_info()

if student1.marks >student2.marks:
    print("Student1 has more marks than student 2")

elif student1.marks < student2.marks:
    print("Student2 has more marks than student ")