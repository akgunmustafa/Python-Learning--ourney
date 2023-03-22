# class
class SoftwareEngineer:
    alias = "Keyboard Magician"

    def __init__(self, name, age, level, salary):
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary


se1 = SoftwareEngineer("Mustafa", 28, "Junior", 5000)
print(se1.name, se1.age)
print(SoftwareEngineer.alias)
se2 = SoftwareEngineer("Cansu", 22, "Junior", 7000)
print(se2.name, se2.age)

# Recap
# create a class (blueprint)
# create a instance (object)
# class vs instance
# instance attributes: defined in __init__(self)
# class attribute