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
        self.starting_health = starting_health
        self.abilities = []
        self.armors = []
        self.current_health = starting_health
        self.deaths = 0
        self.kills = 0
        self.steal = 1

    def add_kill(self, num_kills):
        self.kills = self.kills + num_kills

    def add_deaths(self, num_deaths):
        self.deaths = self.deaths + num_deaths





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

    def add_weapon(self, weapon):
        self.abilities.append(weapon)

    def steal(self):
        if self.steal > 0:
            print(f'Magic gem activated! you have {self.steal} magic sneak chances')
            guess = input('please guess a number between 1 and 10 >')
            pick = randint(0, 10)
            if guess == pick:
            print("wow you actually won!")




#really simple code i love this either true or flase
    def is_alive(self):

        return self.current_health > 0

    def fight(self, opponent):
        if self.is_alive() == True and opponent.is_alive() == True:
            while self.is_alive() == True and opponent.is_alive() == True:
                opponent.take_damage(self.attack())
                self.take_damage(opponent.attack())

                if self.is_alive() == False and opponent.is_alive() == True:
                    print(f'{opponent.name} is Victorious!')
                    opponent.add_kill(1)
                    self.add_deaths(1)
                elif self.is_alive() == True and opponent.is_alive() == False:
                    print(f'{self.name} is Victorious!')
                    self.add_kill(1)
                    opponent.add_deaths(1)
                elif self.is_alive() == False and opponent.is_alive() == False:
                    print("Both heroes are dead.")
                    self.add_kill(1)
                    opponent.add_deaths(1)
                    opponent.add_kill(1)
                    self.add_deaths(1)


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

    def team_members_alive(self):
        heroes_alive = []
        for hero in self.heroes:
            if hero.is_alive() == True:
                heroes_alive.append(hero)
        return heroes_alive
    def num_alive(self):
        number_heroes_alive = 0
        for hero in self.heroes:
            if hero.is_alive() == True:
                number_heroes_alive += 1
        return number_heroes_alive

    def attack(self, other_team):
        while self.num_alive() > 0 and other_team.num_alive() > 0:
            hero1 = random.choice(self.team_members_alive())
            hero2 = random.choice(other_team.team_members_alive())
            hero1.fight(hero2)

    def revive_heroes(self, health=100):
        for hero in self.heroes:
            hero.current_health = 100



    def stats(self):
        for hero in self.heroes:
            if self.deaths > 0 and self.kills > 0:
                kd = self.kills // self.deaths
            elif self.deaths > 0 and self.kills <= 0:
                kd = 0
            else:
                kd = self.kills
        print(f"{self.name} has a kill to death ratio of {kd}")


class Arena:
    def __init__(self):
        self.team_one = None
        self.team_two = None

    def create_ability(self):
        ability_name = input("Name your ability ").lower()
        ability_damage = int(input("How much damage does your ability do? "))
        return Ability(ability_name, ability_damage)
    def create_weapon(self):
        weapon_name = input("Please name your weapon ")
        weapon_damage = int(input("How much damage does your weapon do? "))
        return Weapon(weapon_name, weapon_damage)

    def create_armor(self):
        armor_name = input("What shall we name your armor? ")
        armor_block = int(input("What level of block shall your armor have? "))
        return Armor(armor_name, armor_block)

    def create_hero(self):
        hero_name = input("What would you like to name your hero? ").lower()
        hero_health = int(input("Set hero health "))
        hero = Hero(hero_name, hero_health)

        choose_ability = "YES"
        while choose_ability == "YES":
            ability  = self.create_ability()
            hero.add_ability(ability)
            choose_ability = input("Would you like to add another ability? (Yes or No) ").upper()

        choose_weapon = "YES"
        while choose_weapon == "YES":
            weapon  = self.create_weapon()
            hero.add_weapon(weapon)
            choose_weapon = input("Would you like to add another weapon? (Yes or No) ").upper()

        choose_armor = "YES"
        while choose_armor == "YES":
            armor = self.create_armor()
            hero.add_armor(armor)
            choose_armor = input("Would you like to add more armor? (Yes or No) ").upper()

        return hero

def build_team_one(self):
        team_number = int(input("How many heroes would you like on this team? "))
        team_name = input("Please choose a team name: ")
        self.team_one = Team(team_name)
        for i in range(team_number):
            hero = self.create_hero()
            self.team_one.heroes.append(hero)
            i += 1
            i -= 1
        return self.team_one

def build_team_two(self):
        team_number = int(input("How many heroes would you like on this team? "))
        team_name = input("Please choose a team name: ")
        self.team_two = Team(team_name)
        for i in range(team_number):
            hero = self.create_hero()
            self.team_two.heroes.append(hero)
            i += 1
            i -= 1
        return self.team_two



if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.

    pass
