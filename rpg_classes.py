import random

class Character:
    def __init__(self, name, health, attack, heal, mana):
        self.name = name
        self.health = health
        self.power = attack
        self.heal = heal
        self.mana = mana
        
    def do_attack(self, other):
        other.health -= self.power + (random.randint(0, 20)-10)
    def do_heal(self):
        self.health += self.heal + (random.randint(0, 20)-10)
    def do_magic(self, other):
        other.health -= self.mana + (random.randint(0, 20)-10) 

# 전사 클래스
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack=25, heal=5, mana =0) #각 수치 조정 필요

# 마법사 클래스 
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=80, attack=35, heal=20, mana=30) #각 수치 조정 필요

# 성직자 클래스   
class Priest(Character):
    def __init__(self, name):
        super().__init__(name, health=80, attack=35, heal=20, mana=30) #각 수치 조정 필요

# 고블린1 클래스
class Goblin1(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack=20, heal=0, mana=0) #각 수치 조정 필요
        
# 미믹 클래스
class Mimic(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack=20, heal=0, mana=0) #각 수치 조정 필요
        
# 마왕 클래스 dd
class Boss(Character):
    def __init__(self, name):
        super().__init__(name, health=1000, attack=50, heal=0, mana=0) #각 수치 조정 필요