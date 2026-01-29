# super() is used to call the parent class constructor so that inherited attributes are properly initialized.”
class Employee:
    name = "Muhammad Shahzaib shah"
    def __init__(self):
        print("Emplooyee Constructor")
    def show(self):
        print(f"The Name is {self.name} ")

class Programmer(Employee):
    def __init__(self):
        super().__init__()
        print("Manager Constructor")
    def showLanguage(self):
        print(f"The name is  {self.name}")
a = Programmer()