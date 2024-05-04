from pokemon import Pokemon
from trainer import Trainer

def create_pokemons_and_trainers():
    charmander = Pokemon(1, "Charmander", 8.5, 0.6, "Fire", "Red")
    squirtle = Pokemon(2, "Squirtle", 9.0, 0.5, "Water", "Misty")
    pikachu = Pokemon(3, "Pikachu", 6.0, 0.4, "Electric", "Ash")

    print ("\n\n**** Lista de Pokemons: *****")
    print (charmander, squirtle, pikachu)

    ash = Trainer(1, "Ash", "Ketchum", 10, 5)
    misty = Trainer(2, "Misty", "Waterflower", 8, 6)

    print ("\n\n**** Lista de Entrenadores: *****")
    print (ash, misty, "\n\n")

if __name__ == '__main__':
    create_pokemons_and_trainers()