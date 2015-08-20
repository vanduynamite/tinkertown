from players import *
from occupations import *
from buildings import *


def main():
    player_1 = Player('Paul')
    player_1.add_starting_occupations([Financier,Alchemist],[4,4])
    player_1.list_resources()
    player_1.list_available_workers()

    num_players = 4
    bank = Bank(num_players)
    forge = Forge(num_players)
    workshop = Workshop(num_players)
    townhall = TownHall(num_players)

    player_1.workers[0].go_to_bank(player_1,bank)

    player_1.list_resources()
    bank.list_spots()
if __name__ == "__main__":
    main()