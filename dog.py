# dog .py

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"Woof! says {self.breed} ")

    def sit(self):
        print(f"{self.name} sits down!")

    def roll_over(self):
        print(f"{self.name} rolls over!")
