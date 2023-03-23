# inherits, extend, override
class Employee:

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def work(self):
        print(f"{self.name} is working ...")


class SoftwareEngineer(Employee):
    def work(self):  # override
        print(f"{self.name} is coding ...")

    def __init__(self, name, age, salary, level):
        super().__init__(name, age, salary)
        self.level = level

    def debug(self):
        print(f"{self.name} is debugging... ...")


class Designer(Employee):
    def work(self):  # override
        print(f"{self.name} is designing ...")

    def draw(self):
        print(f"{self.name} is drawing ...")


se1 = SoftwareEngineer("Mustafa", 27, 6000, "Juniour")
print(se1.name, se1.age, se1.level, se1.salary, "$")
se1.work()

se2 = SoftwareEngineer("Canan", 26, 7500, "Senior")
se2.debug()

de = Designer("Cansu", 22, 7000 )
print(de.name, de.age)
de.work()
de.draw()

print("-------------")

# Polymorphism

employees = [SoftwareEngineer("Mustafa", 27, 6000, "Juniour"),
             SoftwareEngineer("Canan", 26, 7500, "Senior"),
             Designer("Cansu", 22, 7000 )]

def motivate_employees(employees):
    for employee in employees:
        employee.work()

motivate_employees(employees)



