import random


class Pokemon:
    def __init__(self, hp, attack_points):
        self.hp = hp
        self.attack_points = attack_points


class Fire(Pokemon):
    def __init__(self, hp, attack_points):
        super().__init__(hp, attack_points)
        self.type = "fire"
        self.weak_type = "water"


class Water(Pokemon):
    def __init__(self, hp, attack_points):
        super().__init__(hp, attack_points)
        self.type = "water"
        self.weak_type = 'electric'


class Ice(Pokemon):
    def __init__(self, hp, attack_points):
        super().__init__(hp, attack_points)
        self.type = "ice"
        self.weak_type = "fire"


class Electric(Pokemon):
    def __init__(self, hp, attack_points):
        super().__init__(hp, attack_points)
        self.type = "electric"
        self.weak_type = "ground"


def attack(attacking_pokemon, defending_pokemon):
    points = 0
    if attacking_pokemon.weak_type.lower() == defending_pokemon.type.lower():
        points = random.random() % attacking_pokemon.attack_points * 0.1
        attacking_pokemon.attack_points = points

    elif defending_pokemon.weak_type.lower() == attacking_pokemon.type.lower():
        points = random.random() % attacking_pokemon.attack_points
        if points * 2 > attacking_pokemon.attack_points:
            points = attacking_pokemon.attack_points
            attacking_pokemon.attack_points = points
        else:
            points = points * 2
            attacking_pokemon.attack_points = points
    else:
        points = random.random() % attacking_pokemon.attack_points

    defending_pokemon.hp -= points
    return defending_pokemon


if __name__ == '__main__':
    pokemon1 = Fire(500, 100)
    pokemon2 = Water(300, 150)
    res = attack(pokemon1, pokemon2)
    print('The {} pokemon hp is {}'.format(res.type, res.hp))
