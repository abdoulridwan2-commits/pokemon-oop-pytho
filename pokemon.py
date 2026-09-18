class Pokemon:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
    def take_damage(self, amount):
        self.hp -= amount
        
        print(f"{self.name} took {amount} damage! HP: {self.hp}")

pikachu = Pokemon("pikachu" , 100)
charmander = Pokemon("charmander" , 90)


pikachu.take_damage(10)