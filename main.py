from game import *

def main():

    game = Game()

    players = {
    1 : [Financier, Alchemist],
    2 : [Blacksmith, Engineer],
    3 : [Financier, Engineer],
    4 : [Blacksmith, Alchemist],
    }

    game.set_up_game(players)

    """This should be a do until every player has gone, or passed. So in Game there should be a check for all players, and in players there should be a default action to pass, and a tag for it as well"""

    for i in range(9):
        game.list_players()

        choose_player = input('Which player? ')
        player = game.players[choose_player]

        game.check_actions(player)
        player.list_actions()
        choose_action = input('Which action? ') - 1
        action = player.place_actions[choose_action]

        player.list_available_workers()
        choose_worker = input('Worker to place? ')
        worker = player.workers[choose_worker - 1]

        action.place_worker(worker)

        

    # player.list_resources()

    # player_1.list_resources()
    # player_1.list_available_workers()
    # player_1.list_actions()

    # player_1.workers[0].go_to_building(bank, player_1)
    # player_1.workers[1].go_to_building(forge, player_1)
    # player_1.workers[2].go_to_building(workshop, player_1)
    # player_1.workers[5].go_to_building(forge, player_1)

    # player_1.list_resources()
    # player_1.list_available_workers()

    # # this call is now obsolete as the available actions are built into player
    # essence_for_jewels = TradeAction('Essence',1,'Jewels',1)
    # essence_for_jewels.trade(player_1,3)
    # # still, it's a good check

    # player_1.list_resources()

if __name__ == "__main__":
    main()