# create a pokemon
# take a look at it
# feed it to increase health
# battle them and find a winner


class Pokemon:
    def __init__(self, name="Default", primary_type="Pokemon", max_hp=0):
        self.name = name
        self.primary_type = primary_type
        self.current_hp = max_hp
        self.max_hp = max_hp

    def __str__(self):
        return f'{self.name} - {self.primary_type}: {self.current_hp}/{self.max_hp}'

    def feed(self):
        if self.current_hp < self.max_hp:
            self.current_hp += 1
            print(f'Current hp of {self.name} is: {self.current_hp}')
        else:
            print(f'{self.name} is already full.')

    def battle(self, other):
        print(f"Battle: {self.name} VS {other.name}")
        result = self.typeWheel(self.primary_type, other.primary_type)
        if result == 'lose':
            self.current_hp = 0
            print(f'{self.name} lost the match!')
        elif result == 'tie':
            self.current_hp -= 10
            other.current_hp -= 10
            print(f'It\'s a tie between {self.name} & {other.name}.')
        elif result == 'win':
            other.current_hp = 0
            print(f"After a hard battle {self.name} won. Congratulations!!!")

    @staticmethod
    def typeWheel(type1, type2):
        result = {0: "lose", 1: "win", -1: "tie"}
        # mapping between types and result conditions
        game_map = {"water": 0, "fire": 1, "grass": 2}

        # implement win-lose matrix condition
        wl_matrix = [
            [-1, 1, 0],  # water - water vs water, water vs fire, water vs grass
            [0, -1, 1],  # fire - fire vs water, fire vs fire, fire vs grass
            [1, 0, -1]  # grass- grass vs water, grass vs fire, grass vs grass
        ]

        # declare a winner
        wl_result = wl_matrix[game_map[type1]][game_map[type2]]
        return result[wl_result]


if __name__ == "__main__":
    b = Pokemon(name="Bulbasaur", primary_type="grass", max_hp=90)
    print(b.name)
    c = Pokemon(name="Charmander", primary_type="fire", max_hp=100)
    print(c.name)
    s = Pokemon('Squirtle', 'water', 115)
    print(s.name)

    print(b)
    b.feed()
    print(b)
    b.battle(c)
    b.battle(b)
    s.battle(c)
