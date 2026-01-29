class Employee:
    def show(self):
        print(f"The Name is {self.name} and tha salary is {self.salary}")

class Programmer(Employee):
    def showLanguage(self):
        print(f"The name is  {self.name}  and he is good with {self .language}")