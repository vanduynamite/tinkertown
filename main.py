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

    """This should be a method in Game. It's fine here for now for testing. So in Game there should be a check for all players, and in players there should be a default action to pass, and a tag for it as well"""

    for i in range(9):
        game.list_players()

        choose_player = input('Which player? ')
        player = game.players[choose_player]

        game.check_actions(player)
        player.list_actions()
        choose_action = input('Which action (just choose a place action for now)? ') - 1
        action = player.place_actions[choose_action]

        player.list_available_workers()
        choose_worker = input('Worker to place? ')
        worker = player.workers[choose_worker - 1]

        action.place_worker(worker)


if __name__ == "__main__":
    main()