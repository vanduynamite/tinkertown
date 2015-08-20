from players import *
from buildings import *


class Worker(object):
	def __init__(self):
		self.starting_resources = {
		'Jewels': 0,
		'Gears': 0,
		'Widgets': 0,
		'Essence': 0,
		}

		self.is_placed = False

		

	def go_to_building(self, building, player):
		#this will look at the building type and add the correct resources to the player, mark the worker as used, and use a building spot

		if building.is_available():
			#resources = self.building_resources(type(building))
			#player.add_resources(resources)
			building.use_spot()
			self.is_placed = True
			return True
		else:
			print '%s is full!' % building.name
			return False


class Financier(Worker):
	def __init__(self):
		Worker.__init__(self)
		self.name = 'Financier'
		self.starting_resources['Jewels'] = 2
		
		# bank_resources = {
		# 'Jewels' : 2,
		# }

		# forge_resoures = {
		# 'Jewels' : 1,
		# 'Gears' : 1,
		# }

		# workshop_resources = {
		# 'Jewels' : 1,
		# 'Widgets' : 1,
		# }

		# self.building_resources = {
		# type(Bank) : bank_resources,
		# type(Forge) : forge_resoures,
		# type(Workshop) : workshop_resources,
		# }


class Blacksmith(Worker):
	def __init__(self):
		Worker.__init__(self)
		self.name = 'Blacksmith'
		self.starting_resources['Jewels'] = 1
		self.starting_resources['Gears'] = 3

class Engineer(Worker):
	def __init__(self):
		Worker.__init__(self)
		self.name = 'Engineer'
		self.starting_resources['Jewels'] = 1
		self.starting_resources['Widgets'] = 1

class Alchemist(Worker):
	def __init__(self):
		Worker.__init__(self)
		self.name = 'Alchemist'
		self.starting_resources['Essence'] = 2