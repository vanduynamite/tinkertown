from players import *
from occupations import *


def main():
    player_1 = Player('Audrey')
    player_1.add_starting_occupations([Engineer,Alchemist],[4,4])
    player_1.list_resources()
    player_1.list_workers()

if __name__ == "__main__":
    main()