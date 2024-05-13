from trainer import Trainer
class Pokemon:
    def __init__(self, id:int, name:str, weight:float, height:float, trainer:Trainer ) -> None:
        self.__id=id
        self.name=name
        self.weight = weight
        self.height = height
        self.trainer = trainer
        
    def __str__(self)  ->str:
        return self.name
    
    def get_id(self):
        return self.__id
    
    def set_id(self, id):
        if isinstance(id, int):
            self.__id = id
        else:
            raise TypeError("El Id deber ser un entero")
        
    def attack(self):
        return f"{self.name} lanzó un ataque"
        
class ElectricPokemon(Pokemon):
    def attack(self):
        return f"{self.name} lanzó un ataque eléctrico!"

class WaterPokemon(Pokemon):
    def attack(self):
        return f"{self.name} lanzó un ataque acuático!"

class FirePokemon(Pokemon):
    def attack(self):
        return f"{self.name} lanzó un ataque de fuego!"
