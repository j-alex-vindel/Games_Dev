import items

class NonPlayableCharacter():
    def __init__(self):
        raise NotImplementedError('Do not create raw NPC objects.')

    def __str__(self):
        return self.name

class Trader(NonPlayableCharacter):
    def __init__(self):
        self.name = "Oscar & Willow's shop"
        self.gold = 100
        self.inventory = [items.CrustyBread(),items.GreenHerb(),
                          items.GreenHerb(),items.GreenHerb()]
