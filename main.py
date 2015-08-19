from players import *
from occupations import *


def main():
    player_1 = Player()
    player_1.add_starting_occupations([Financier,Blacksmith],[4,4])
    player_1.list_resources()
    #print 'Checking Jewels... ', player_1.resources['Jewels']
    player_1.list_workers()

if __name__ == "__main__":
    main()