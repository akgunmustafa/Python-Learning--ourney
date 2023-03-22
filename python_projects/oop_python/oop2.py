# class
class SoftwareEngineer:
    # instance attributes
    def __init__(self, name, age, level, salary):
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary

    # instance method
    def code(self):
        print(f"{self.name} is writing code...")

    def code_in_language(self, language):
        print(f"{self.name} is writing code in {language}...")

    # def information(self):
    #     information = f"name={self.name}, age={self.age}, level={self.level} "
    #     return information

    # dunder method
    def __str__(self):
        information = f"name={self.name}, age={self.age}, level={self.level} "
        return information

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    @staticmethod
    def entry_salary(age):
        if age < 25:
            return 5000
        if age > 25:
            return 7000
        return 9000


# instance
se1 = SoftwareEngineer("Mustafa", 22, "Junior", 5000)
se2 = SoftwareEngineer("Cansu", 22, "Senior", 7000)

se1.code()
se2.code()
se1.code_in_language("Java")
se2.code_in_language("C++")

# print(se1 == se2)
# print(se1)

print(se1.entry_salary(20))
print(SoftwareEngineer.entry_salary(24))
