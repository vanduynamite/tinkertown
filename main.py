from players import *
from workers import *
from buildings import *
from abilities import *
from machines import *


def main():
    player_1 = Player('Paul')
    player_1.add_starting_occupations([Alchemist, Financier],[4,4])

    num_players = 4
    bank = Bank(num_players)
    forge = Forge(num_players)
    workshop = Workshop(num_players)
    townhall = TownHall(num_players)


    player_1.list_resources()
    player_1.list_available_workers()
    player_1.list_abilities()

    player_1.workers[0].go_to_building(bank, player_1)
    player_1.workers[1].go_to_building(forge, player_1)
    player_1.workers[2].go_to_building(workshop, player_1)
    player_1.workers[5].go_to_building(forge, player_1)

    player_1.list_resources()
    player_1.list_available_workers()

    # this call is now obsolete as the available abilities are built into player
    essence_for_jewels = TradeAbility('Essence',1,'Jewels',1)
    essence_for_jewels.trade(player_1,3)
    # still, it's a good check

    player_1.list_resources()

if __name__ == "__main__":
    main()