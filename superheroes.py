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
        self.deaths = 0
        self.kills = 0

    def add_kill(self, num_kills):
        self.kills = self.kills + num_kills

    def add_deaths(self, num_deaths):
        self.deaths = self.deaths = num_deaths





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
    def attack(self):
        att = random.randint(self.attack_strength // 2, self.attack_strength)
        return att

class Team:
    def __init__(self, name):
        self.name = name
        self.heroes = []

    def remove_hero(self, name):
        index = 0
        length = len(self.heroes)
        for hero in self.heroes:
            if hero.name == name:
                del self.heroes[index]
            else:
                index += 1
        if len(self.heroes) == length:
            return 0


    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero.name)

        '''Prints out all heroes to the console.'''

        # TODO: Loop over the list of heroes and print their names to the terminal.

    def add_hero(self, hero):

        self.heroes.append(hero)


if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.

    pass
