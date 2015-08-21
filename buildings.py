from game import *

class Building(object):
	# basic building. Has some spots, has available spots. Has a couple methods.

	def __init__(self):
		self.name = ''
		self.available_spots = 0
		self.open_spots = 0

	def is_available(self):
		# a check to see if the building is available at all. Should be used by everything that calls this building before it's called.
		return self.open_spots > 0

	def list_spots(self):
		# To list, if needed.
		print '%s has %s open spots' % (self.name, str(self.open_spots))

	def use_spot(self):
		# Will mark a spot as used. Has a check just in case the method calling it didn't check first.
		if self.open_spots >= 1:
			self.open_spots -= 1
			return True
		else:
			print '%s is full! (from Building class)' % self.name
			return False

class Bank(Building):
	def __init__(self, players):
		# Set the name and number of spots by number of players
		Building.__init__(self)
		self.name = 'Bank'

		spot_list = {
		2 : 3,
		3 : 5,
		4 : 6,
		5 : 7,
		6 : 8,
		}

		self.available_spots = spot_list[players]
		self.open_spots = self.available_spots


class Forge(Building):
	def __init__(self, players):
		# Set the name and number of spots by number of players
		Building.__init__(self)
		self.name = 'Forge'

		spot_list = {
		2 : 2,
		3 : 3,
		4 : 4,
		5 : 5,
		6 : 6,
		}

		self.available_spots = spot_list[players]
		self.open_spots = self.available_spots

class Workshop(Building):
	def __init__(self, players):
		# Set the name and number of spots by number of players
		Building.__init__(self)
		self.name = 'Workshop'

		spot_list = {
		2 : 2,
		3 : 3,
		4 : 4,
		5 : 5,
		6 : 6,
		}

		self.available_spots = spot_list[players]
		self.open_spots = self.available_spots

class TownHall(Building):
	def __init__(self, players):
		# Set the name and number of spots by number of players
		Building.__init__(self)
		self.name = 'Town Hall'

		spot_list = {
		2 : 4,
		3 : 5,
		4 : 6,
		5 : 7,
		6 : 8,
		}

		self.available_spots = spot_list[players]
		self.open_spots = self.available_spots