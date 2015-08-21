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

    for i in range(5):
        game.list_players()

        choose_player = input('Which player? ')
        player = game.players[choose_player]

        game.check_actions(player,['trigger_game_start','trigger_trade'])
        player.list_actions()
        choose_action = input('Which action? ') - 1
        action = player.actions[choose_action]

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