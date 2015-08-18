from players import *
from occupations import *


def main():
    player_1 = Player()
    player_1.list_resources()
    print player_1.resources['Jewels']

if __name__ == "__main__":
    main()