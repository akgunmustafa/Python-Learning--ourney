class Dog:
    species = "None Familiars"

    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"


panda = Dog("Panda", 5, "brown")
print(f"{panda.name}'s coat is {panda.color}")
print(panda)
print(panda.speak("auuu"))
