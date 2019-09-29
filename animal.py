class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print('{} is eating.'.format(self.name))

    def sleep(self):
        print(f'{self.name} is sleeping')

animal = Animal("Doggo")

animal.eat()
animal.sleep()
