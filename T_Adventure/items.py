class Weapon:
    def __init__(self):
        raise NotImplementedError('Do not create raw Weapon objects.')
    def __str__(self):
        return self.name


class Rock(Weapon):
    def __init__(self):
        self.name = 'Rock'
        self.description = 'Afist-sized rock, suitable for bludgeoning.'
        self.damage = 5
        self.value = 1

class Dagger(Weapon):
    def __init__(self):
        self.name = 'Dagger'
        self.description = 'A small dagger with some rust. Somewhat more dangerous than a rock.'
        self.damage = 10
        self.value = 20

class RustySword(Weapon):
    def __init__(self):
        self.name = 'Rusty Sword'
        self.description = 'This sword is showing its age, but still has some fight in it.'
        self.damage = 20
        self.value = 100

class Axe(Weapon):
    def __init__(self):
        self.name = 'Axe'
        self.description = 'A mighty axe'
        self.damage = 25
        self.value = 150

class Consumable:
    def __init__(self):
        raise NotImplementedError('Do not create raw Consumable objects.')

    def __str__(self):
        return '{}(+{} HP)'.format(self.name,self.healing_value)

class CrustyBread(Consumable):
    def __init__(self):
        self.name = 'CrustyBread'
        self.healing_value = 10
        self.value = 12

class GreenHerb(Consumable):
    def __init__(self):
        self.name = 'GreenHerb'
        self.healing_value = 5
        self.value = 7
