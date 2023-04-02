import random
import enemies
import player
import npc

class Maptile:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def intro_text(self):

        raise NotImplementedError('Create a subclass instead')

    def modify_player(self,player):
        pass

class StartTile(Maptile):

    def intro_text(self):
        return """
        You find yourself in a cave with a flickering torch on the wall.
        You can make out four paths, each equally as dark and foreboding.
         """

class BoringTile(Maptile):

    def intro_text(self):
        return """
        This is a very boring part of the cave.
         """

class VictoryTile(Maptile):

    def modify_player(self, player):
        player.victory = True

    def intro_text(self):
        return """
        Youe see a bright light in the distance....
        ... it grows as you get closer! it's sunlight!


        Victory is yours! """

class Waterfall(Maptile):
    def intro_text(self):
        return """
        Hidden in the caves there's a light coming from the ceiling...
        Someting can be heard....

        It seems like a river inside a cave...

        It's a waterfall... that comes through a crack in the rock.... """

class Lake(Maptile):
    def intro_text(self):
        return """
        The waterfall makes a lake inside the caverns...
        I hear something in the water... I must run... back """

class Ray_ofhope(Maptile):
    def intro_text(self):
        return"""

        The ligh seems brighter ans shines upon this stream of water that further down makes a loud noise """

class Darktile(Maptile):
    def intro_text(self):
        return """
        There's only darkness here... """

class Fossils(Maptile):
    def intro_text(self):
        return """
        What a unique set of rocks....

        They're not rocks... on a closer look, they look like bones!

        ...

        ...
        They're not human, it seems like a giant lizard..."""

class Blocked(Maptile):
    def intro_text(self):
        return """
        This passage seems to be blocked..."""

class EnemyTile(Maptile):
    def __init__(self,x,y):
        r = random.random()
        if r < .5:
            self.enemy = enemies.GiantSpider()
            self.alive_text = """ A giant spider jumps down from
            its web in front of you... """
            self.dead_text = """ The corpse of a dead spider
                                rots on the ground"""
        elif r < .8:
            self.enemy = enemies.Ogre()
            self.alive_text = """ An Ogre is blockig your path!"""
            self.dead_text = """ A dead Ogre stinks this hall and it reminds you of your triumph"""

        elif r < .95:
            self.enemy = enemies.BatColony()
            self.alive_text = """ What is this sqeaking noise...?

                                  It get's louder and louder...

                                  Suddenly your are lost in a swarm of bats!"""
            self.dead_text = """ Dozens of dead bats are scattered on the ground, there's still some blood on their fangs"""
        else:
            self.enemy = enemies.RockMonster()
            self.alive_text = """ Your steps have disturbed a rock monster from his slumber....."""
            self.dead_text = """ Defeated, the monster has crumbled into a pile of ordinary rocks"""

        super().__init__(x,y)

    def intro_text(self):
        text = self.alive_text if self.enemy.is_alive() else self.dead_text
        return text

    def modify_player(self,player):
        if self.enemy.is_alive():
            player.hp = player.hp - self.enemy.damage
            print('Enemy does {} damage. You have {} HP left.'.format(self.enemy.damage,player.hp))

class FindGoldTile(Maptile):
    def __init__(self, x, y):
        self.gold = random.randint(1,50)
        self.gold_claimed = False
        super().__init__(x, y)

    def modify_player(self, player):
        if not self.gold_claimed:
            self.gold_claimed = True
            player.gold = player.gold + self.gold
            print("+{} gold added.".format(self.gold))

    def intro_text(self):
        if self.gold_claimed:
            return '''
            Another unremarkable part of the cave. You must forge onwards.'''
        else:
            return '''
            Someone dropped some gold. You pick it up.'''


class TraderTile(Maptile):

    def __init__(self,x,y):
        self.trader = npc.Trader()

        super().__init__(x,y)

    def trade(self, buyer, seller):
        for i, item in enumerate(seller.inventory, 1):
            print('{}. {} - {} Gold'.format(i, item.name, item.value))

        while True:
            user_input = input('Choose an item or press Q to exit: ')
            if user_input in ['q', 'Q']:
                return
            else:
                try:
                    choice = int(user_input)
                    to_swap = seller.inventory[choice-1]
                    self.swap(seller, buyer, to_swap)
                except ValueError:
                    print('Invalid Choice!')

    def swap(self, seller, buyer, item):
        if item.value > buyer.gold:
            print("That's to expensive")
            return
        seller.inventory.remove(item)
        buyer.inventory.append(item)
        seller.gold = seller.gold + item.value
        buyer.gold = buyer.gold - item.value
        print('Trade Complete!')

    def check_if_trade(self, player):
        while True:
            print('Would you like to (B)uy, (S)ell, or (Q)uit?')
            user_input = input()
            if user_input in ['Q','q']:
                return
            elif user_input in ['B','b']:
                print("Here's what's available to buy: ")
                self.trade(buyer=player, seller=self.trader)
            elif user_input in ['S','s']:
                print("Here's what's available to sell: ")
                self.trade(buyer=self.trader, seller=player)
            else:
                print('Invalid Choice!')

    def intro_text(self):
        return '''
        A frail not-quite-human, note-quite-creature peaks over a crack in the rock...

        Clicking its gold coins together. It must be a place to trade '''


world_dsl = '''
|RH|VT|EN|TT|EN|
|EN|EN|FG|FO|BT|
|TT|EN|EN|EN|DT|
|WF|BT|BT|EN|EN|
|FG|EN|ST|FO|EN|
|LA|DT|BL|DT|FG|
'''

def is_dsl_valid(dsl):
    if dsl.count('|ST|') != 1:
        return False
    if dsl.count('|VT|') == 0:
        return False
    lines = dsl.splitlines()
    lines = [l for l in lines if l]
    pipe_counts = [line.count('|') for line in lines]
    for count in pipe_counts:
        if count != pipe_counts[0]:
            return False
    return True

tile_type_dict = {'VT':VictoryTile,'EN':EnemyTile,'ST':StartTile,
'RH':Ray_ofhope,'FO':Fossils,'WF':Waterfall,'LA':Lake,
'BL':Blocked,'DT':Darktile,
'TT':TraderTile,'FG':FindGoldTile,'BT':BoringTile}

world_map = []

# world_map = [
#              [Ray_ofhope(0,0),VictoryTile(1,0),EnemyTile(2,0)],
#              [EnemyTile(0,1),EnemyTile(1,1),Fossils(2,1)],
#              [Waterfall(0,2),StartTile(1,2),EnemyTile(2,2)],
#              [Lake(0,3),Blocked(1,3),Darktile(2,3)]
#              ]

start_tile_location = None

def parse_world_dsl():
    if not is_dsl_valid(world_dsl):
        raise SyntaxError('DSL is invalid!')

    dsl_lines = world_dsl.splitlines()
    dsl_lines = [x for x in dsl_lines if x]

    for y, dsl_row in enumerate(dsl_lines):
        row = []
        dsl_cells = dsl_row.split('|')
        dsl_cells = [c for c in dsl_cells if c]
        for x, dsl_cell in enumerate(dsl_cells):
            tile_type = tile_type_dict[dsl_cell]
            if tile_type == StartTile:
                global start_tile_location
                start_tile_location = x, y
            row.append(tile_type(x, y) if tile_type else None)

        world_map.append(row)

def tile_at(x,y):
    if x < 0 or y < 0:
        return None
    try:
        return world_map[y][x]
    except IndexError:
        return None
