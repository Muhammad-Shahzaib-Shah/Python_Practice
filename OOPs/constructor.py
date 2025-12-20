class Employee:
    language = "Python"
    salary = 1000
    def __init__(self , name , salary, language):#Dunder Method which is automatically called
        self.language = language
        self.salary = salary
        self.name = name
        print("creating Object")
    @staticmethod
    def greet():
        print("Good Morning")
    def getInfo(self):
        #“self is used to refer to the current object so that each object can maintain its own data.”
        print(f"The language is {self.language} and the salary is {self.salary}")
shato = Employee("Muhammad Shahzaib Shah", 20000 , "JS")
print(shato.name,shato.salary, shato.language)