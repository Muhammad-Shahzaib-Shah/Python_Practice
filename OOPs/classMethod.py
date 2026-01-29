class Employee:
    a =2
    @classmethod
    def show(cls):
        print(f"a is {cls.a}")
        
o = Employee()
o.a = 20
o.show()
#“A class method works with class-level data and receives the class itself as its first parameter, conventionally named cls.”
class Employees:
    company = "Google"   # class variable

    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company
e1 = Employees()
e2 = Employees()

Employees.change_company("OpenAI")

print(Employees.company)  # OpenAI

