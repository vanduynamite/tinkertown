from game import *

def main():

    game = Game()

    players = {
    'Evan' : [Financier, Alchemist],
    'Lorenzo' : [Blacksmith, Engineer],
    'Roland' : [Financier, Engineer],
    'Josh' : [Blacksmith, Alchemist],
    }

    game.run_game(players)


if __name__ == "__main__":
    main()