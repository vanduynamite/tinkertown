class Building(object):
	def __init__(self):
		self.name = ''
		self.available_spots = 0
		self.open_spots = 0

	def is_available(self):
		return self.open_spots > 0

	def list_spots(self):
		print '%s has %s open spots' % (self.name, str(self.open_spots))

	def use_spot(self):
		if self.open_spots >= 1:
			self.open_spots -= 1
		else:
			print '%s is full! (from Building class)' % self.name

class Bank(Building):
	def __init__(self, players):
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