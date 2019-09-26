import random

class Ability:
    def __init__(self, name, attack_strength):
        self.name = name
        self.attack_strength = attack_strength

    def attack(self):
        att = random.randint(0, self.attack_strength)
        return att

class Armor:
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block

    def block(self):
        block = random.randint(0, self.max_block)
        return block

class Hero:
    def __init__(self, name, starting_health):
        self.name = name
        self.starting_heatlh = starting_health
        self.abilities = []
        self.armors = []
        self.current_health = starting_health

    def add_ability(self, ability):
        """ Add Ability"""

        return self.abilities.append(ability)

    def attack(self):

        return sum([ability.attack() for ability in self.abilities])

    def add_armor(self, armor):

        self.armors.append(armor)

    def defend(self):

        return sum([armor.block() for armor in self.armors])

    def take_damage(self, damage):
        self.current_health -= max(0, damage - self.defend())

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block of code is executed.

    hero = Hero("Grace Hopper", 200)
    shield = Armor("Shield", 50)
    hero.add_armor(shield)
    hero.take_damage(50)
    print(hero.current_health)
