from players import *
from buildings import *
from abilities import *
from machines import *

# All resources (hopefully everywhere?) will be communicated via dictionaries
# This way the amount of resources doesn't matter. If later a new one is added, no problem
# Or, if in many situations, you only need to send one or two, that's fine.

class Worker(object):
	def __init__(self):
		# nothing to see here except the is_placed
		# and of course common methods

		self.is_placed = False

		
	def go_to_building(self, building, player):
		#this will look at the building type and add the correct resources to the player, mark the worker as used, and use a building spot

		if self.is_placed:
			print 'This %s is already used!' % self.name
			return False

		else:

			if building.is_available():
				resources = self.building_resources[type(building)]
				player.add_resources(resources)
				building.use_spot()
				self.is_placed = True
				return True
			else:
				print '%s is full!' % building.name
				return False

	def set_building_resources(self, bank_resources, forge_resoures, workshop_resources):

		self.building_resources = {
		type(Bank(4)) : bank_resources,
		type(Forge(4)) : forge_resoures,
		type(Workshop(4)) : workshop_resources,
		}


class Financier(Worker):
	def __init__(self):
		# set the name and all the resource combinations
		Worker.__init__(self)
		self.name = 'Financier'

		self.starting_resources = {
		'Jewels': 2,
		}

		bank_resources = {
		'Jewels' : 2,
		}

		forge_resoures = {
		'Jewels' : 1,
		'Gears' : 1,
		}

		workshop_resources = {
		'Jewels' : 1,
		'Widgets' : 1,
		}

		self.set_building_resources(bank_resources, forge_resoures, workshop_resources)


class Blacksmith(Worker):
	def __init__(self):
		# set the name and all the resource combinations
		Worker.__init__(self)
		self.name = 'Blacksmith'

		self.starting_resources = {
		'Jewels': 1,
		'Gears': 3,
		'Widgets': 0,
		'Essence': 0,
		}

		bank_resources = {
		'Jewels' : 1,
		}

		forge_resoures = {
		'Gears' : 3,
		}

		workshop_resources = {
		'Gears' : 1,
		'Widgets' : 1,
		}

		self.set_building_resources(bank_resources, forge_resoures, workshop_resources)

class Engineer(Worker):
	def __init__(self):
		# set the name and all the resource combinations
		Worker.__init__(self)
		self.name = 'Engineer'

		self.starting_resources = {
		'Jewels': 1,
		'Widgets': 1,
		}

		bank_resources = {
		'Jewels' : 1,
		}

		forge_resoures = {
		'Gears' : 2,
		}

		workshop_resources = {
		'Widgets' : 2,
		}

		self.set_building_resources(bank_resources, forge_resoures, workshop_resources)

class Alchemist(Worker):
	def __init__(self):
		# set the name and all the resource combinations
		Worker.__init__(self)
		self.name = 'Alchemist'

		self.starting_resources = {
		'Essence': 2,
		}

		bank_resources = {
		'Jewels' : 1,
		'Essence' : 1,
		}

		forge_resoures = {
		'Essence' : 1,
		'Gears' : 1,
		}

		workshop_resources = {
		'Essence' : 1,
		'Widgets' : 1,
		}

		self.set_building_resources(bank_resources, forge_resoures, workshop_resources)