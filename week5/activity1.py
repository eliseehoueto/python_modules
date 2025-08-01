class SuperHero:
    def __init__(self,name,power):
        self.name = name
        self.power = power
        self.life=100
        
    def attack(self):
        if self.life<20 :
            print('Game over')
        else:
            self.life-=20
            print("Impact***")
            
superman= SuperHero('Karl', 'SuperForce')
superman.attack()
superman.attack()
superman.attack()
superman.attack()
superman.attack()
superman.attack()
superman.attack()
