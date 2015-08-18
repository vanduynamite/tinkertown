import pdb
import numpy
import random

class Player(object):
    def __init__(self):
        self.default_replacement_stack = [1,1,1,1,2,2,2,2,3,3,3,3]
        self.replacement_stack = []

        
    def hello(self):
    	print "Hello."

def main():
    player_1 = Player()
    player_1.hello()

if __name__ == "__main__":
    main()