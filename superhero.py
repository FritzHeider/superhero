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
        self.armor = []
        self.current_health = starting_health

    def add_ability(self, ability):
        """ Add Ability"""

        return self.abilities.append(ability)

    def attack(self):
        i = 0
        for ability in self.abilities:
            i = i + ability.attack()

        return i

    def add_armor(self, armor):

        return self.armor.append(armor)

    def defend(self, damage_amt):
        i = 0
        for block in self.armor:
            i = i + armor.block

        return i


if __name__ == "__main__":
    # If you run this file from the terminal
    # this block of code is executed.
    ability = Ability("Great Debugging", 50)
    another_ability = Ability("Smarty Pants", 90)
    hero = Hero("Grace Hopper", 200)
    hero.add_ability(ability)
    hero.add_ability(another_ability)
    print(hero.attack())
