#my-dogs.py
from dog import *

my_dog = Dog("Rex", "superdog")
#my_dog.breed = "Super Dog"

print(my_dog)
print(my_dog.name)
print(my_dog.breed)

my_dog.bark()
my_dog.sit()


my_other_dog = Dog("Annie", "Akita")
print(my_other_dog.name)

my_third_dog = Dog("Klaimo", "little boy")

my_third_dog.roll_over()
my_other_dog.sit()
