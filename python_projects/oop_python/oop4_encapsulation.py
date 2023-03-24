

class SoftwareEngineer:
    def __init__(self, name, age):
        self.name=name
        self.age=age
        self._salary=None
        self._num_bugs_solved=0

    # getter
    def get_salary(self):
        return self._salary

    # setter
    def set_salary(self, value):
        # check value, enforce constraints
        if value <1000:
            self._salary = 1000
        if value > 20000:
            self._salary = 20000
        self._salary = value

se = SoftwareEngineer("Mustafa", 25)
print(se.age, se.name,)

se.set_salary(6000)
print(se.get_salary())