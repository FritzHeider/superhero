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
    def __init__(self, name, starting_health=100):
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


#really simple code i love this either true or flase
    def is_alive(self):

        return self.current_health > 0

    def fight(self, opponent):
        if not self.abilities and not opponent.abilities:
            print('Draw!')
            return

        while self.is_alive() and opponent.is_alive():
            self.take_damage(opponent.attack())
            opponent.take_damage(self.attack())

        if self.is_alive():
            print(f"{opponent.name} has died")
        elif opponent.is_alive():
            print(f"{self.name} is is dead!")
        else:
            print("both heros have died!")

class Weapon(Ability):
 """Subclass of Ability"""
    def attack(self):
        att = random.randint(self.attack_strength // 2, self.attack_strength)
        return att



  #
  # ''' Current Hero will take turns fighting the opponent hero passed in.
  # '''
  # TODO: Fight each hero until a victor emerges.
  # Print the victor's name to the screen.
if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.

    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 200)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 180)
    ability4 = Ability("Wizard Beard", 120)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)
