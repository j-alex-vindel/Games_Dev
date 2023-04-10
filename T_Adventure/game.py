from collections import OrderedDict
from player import Player
import world


# There are still some improvements to be made, add some more tiles,
# loot from enemies, magic and side quests

def play():

    print('Escape from Cave Terror!')
    world.parse_world_dsl()
    player = Player()
    while player.is_alive() and not player.victory:
        room = world.tile_at(player.x,player.y)
        print(room.intro_text())
        room.modify_player(player)
        if player.is_alive() and not player.victory:

            choose_action(room, player)
        elif not player.is_alive():
            print('Your journey has come to an early end!')

        # action_input = get_player_command()
        # if action_input in ['n','N']:
        #
        #     player.move_north()
        # elif action_input in  ['s','S']:
        #
        #     player.move_south()
        # elif action_input in ['e','E','>']:
        #
        #     player.move_east()
        # elif action_input in ['w','W','<']:
        #
        #     player.move_west()
        # elif action_input in ['i','I']:
        #     player.print_inventory()
        # elif action_input in ['a','A']:
        #     player.attack()
        #
        # elif action_input in ['h','H']:
        #     player.heal()
        # else:
        #     print('Invalid action!')

# def get_player_command():
#     return input('Action: ')
def choose_action(room, player):
    action = None
    while not action:
        available_actions = get_available_actions(room, player)
        action_input = input('Action: ')
        action = available_actions.get(action_input)
        if action:
            action()
        else:
            print('Invalid Action!')

def get_available_actions(room, player):
    actions = OrderedDict()
    print('Choose an action: ')

    if player.inventory:
        action_adder(actions, 'i', player.print_inventory, 'Print Inventory')
    if isinstance(room, world.TraderTile):
        action_adder(actions, 't',player.trade, 'Trade')
    if isinstance(room,world.EnemyTile) and room.enemy.is_alive():
        action_adder(actions, 'a', player.attack, 'Attack')
    else:
        if world.tile_at(room.x,room.y-1):
            action_adder(actions,'n',player.move_north,'Go North')
        if world.tile_at(room.x,room.y+1):
            action_adder(actions,'s',player.move_south,'Go South')
        if world.tile_at(room.x+1,room.y):
            action_adder(actions,'e',player.move_east,'Go East')
        if world.tile_at(room.x-1,room.y):
            action_adder(actions,'w',player.move_west,'Go West')

    if player.hp < 100:
        action_adder(actions, 'h', player.heal, 'Heal')

    return actions

def action_adder(action_dict, hotkey, action, name):
    action_dict[hotkey.lower()] = action
    action_dict[hotkey.upper()] = action
    print('{}: {}'.format(hotkey,name))


if __name__ == '__main__':
    play()
