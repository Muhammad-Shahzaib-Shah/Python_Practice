class Employee:
    language = "Python"
    Salary = 1000
    @staticmethod
    def greet():
        print("Good Morning")
    def getInfo(self):
        #“self is used to refer to the current object so that each object can maintain its own data.”
        print(f"The language is {self.language} and the salary is {self.Salary}")
shato = Employee()
shato.name = "Muhammad Shahzaib Shah"
shato.getInfo()
shato.greet()