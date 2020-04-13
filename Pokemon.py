# Give Pokémon experience for battling other Pokémon.
# A Pokémon’s level should increase once it gets enough experience points.

class Pokemon:
    def __init__(self, name, level, health, max_health, type, experience):
        self.name = name
        self.level = level
        self.health = health
        self.max_health = max_health
        self.type = type
        if health == 0:
            self.is_knocked_out = True
        else:
            self.is_knocked_out = False
        self.experience = experience

    def gain_experience(self):

        if self.experience >= 500:
            self.level += 1
            self.experience -= 500
            print(f'{self.name} levelled up to {self.level} and the experience is {self.experience}')
        else:
            print(f'{self.name} experience is now {self.experience}')

    def knock_out(self):
        self.is_knocked_out = True

    def revive(self):
        self.is_knocked_out = False

    def lose_health(self, health_lost):
        self.health -= health_lost
        if self.health > 0:
            print(f'{self.name} now has {self.health} health')
        else:
            self.knock_out()
            print(f'{self.name} is knocked out')
            self.health = 0

    def regain_health(self, health_gained):
        self.revive()
        self.health += health_gained
        if self.health > self.max_health:
            self.health = self.max_health
            print(f'{self.name} now has {self.health} health (to the max)')
        else:
            print(f'{self.name} now has {self.health} health')

    def attack(self, other_pokemon):
        damage = 0
        if self.is_knocked_out is True:
            print('Attacking Pokemon is knocked out')
        else:
            s = self.type 
            o = other_pokemon.type
            if s == 'fire' and o == 'grass' or s == 'grass' and o == 'water' or s == 'water' and o == 'fire':
                damage = 2 * self.level
            elif s == 'grass' and o == 'fire' or s == 'fire' and o == 'fire' or s == 'grass' and o == 'grass' or s == 'water' and o == 'water' or s == 'fire' and o == 'water' or s == 'water' and o == 'grass':
                damage = 0.5 *self.level

            other_pokemon.lose_health(damage)
            self.gain_experience()


class Charmander(Pokemon):
    def jump(self):
        print(f'Charmander {self.name} jumped like no Pokemon could')


class Trainer:

    def __init__(self, list_pokemon, name, number_potions, active_pokemon):
        if len(list_pokemon) < 7:
            self.list_pokemon = list_pokemon
        else:
            print('Trainer can have up to 6 Pokemons')
        self.name = name
        self.number_potions = number_potions
        self.active_pokemon = active_pokemon

    def use_potion(self):  # gives active pokemon 200 health
        if self.number_potions > 0:
            self.active_pokemon.regain_health(200)
            self.number_potions -= 1
            print(f'Potion count {self.number_potions}')
        else:
            print("Trainer doesn't have potions")

    def attack_other_trainer(self, other_trainer):
        print(f"{self.name}'s pokemon {self.active_pokemon.name} attacked {other_trainer.name}'s pokemon {other_trainer.active_pokemon.name}")
        self.active_pokemon.attack(other_trainer.active_pokemon)

    def switch_active(self, new_active_pokemon):
        if new_active_pokemon in self.list_pokemon and new_active_pokemon.is_knocked_out is False:
            self.active_pokemon = new_active_pokemon
            print(f"{self.name}'s active pokemon is now {self.active_pokemon.name}")
        elif new_active_pokemon in self.list_pokemon and new_active_pokemon.is_knocked_out is True:
            print(f"{new_active_pokemon.name} is knocked out")
        elif new_active_pokemon not in self.list_pokemon and new_active_pokemon.is_knocked_out is False:
            print(f"{new_active_pokemon.name} is not in {self.name}'s pokemon list")
        elif new_active_pokemon not in self.list_pokemon and new_active_pokemon.is_knocked_out is True:
            print(f"{new_active_pokemon.name} is not in {self.name} list and is knocked out")

    def add_potion(self, number):
        self.number_potions += number
        print(f'{self.name} now has {self.number_potions} potions')


picachu = Pokemon('Picachu', 55, 0, 1000, 'Fire', 400)
dinosaur = Pokemon('Dinosaurus', 60, 200, 1599, 'Grass', 400)
charru = Charmander('Chaka-ckaha', 15, 150, 800, 'Water', 200)

saruman = Trainer([picachu, dinosaur], 'Saruman', 5, dinosaur)
gandalf = Trainer([picachu, dinosaur], 'Gandalf', 7, picachu)

print(dinosaur.experience)
charru.jump()
saruman.attack_other_trainer(gandalf)

