class Player:
    def __init__(self,name,health=100):
        self.name = name
        self.health = health
        self.level = 1


    MAX_LEVEL = 40

    def __str__(self):
        return f"<{self.name}:{self.level}, {self.health} HP>"


    def __repr__(self):
        return f"<{self.name}:{self.level}, {self.health} HP>"


    def __lt__(self,other):
        return (self.health < other.health) if (self.level == other.level) else (self.level < other.level)
    def __gt__(self,other):
        return (self.health > other.health) if (self.level == other.level) else (self.level > other.level)
    def __le__(self,other):
        return (self.health <= other.health) if (self.level == other.level) else (self.level < other.level)
    def __ge__(self,other):
        return (self.health >= other.health) if (self.level == other.level) else (self.level > other.level)
    def __eq__(self,other):
        return self.health == other.health and self.level == other.level
    def __ne__(self,other):
        return self.level != other.level


    def take_hit(self,damage):
        self.health -= damage


    def heal(self, amount):
        self.health += amount


    def level_up(self):
        self.level += 1
        self.health = 100


    @staticmethod
    def find_strongest(players):
        return max(players)
