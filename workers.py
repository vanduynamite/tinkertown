from game import *
from actions import *
from buildings import *

# All resources (hopefully everywhere?) will be communicated via dictionaries
# This way the amount of resources doesn't matter. If later a new one is added, no problem
# Or, if in many situations, you only need to send one or two, that's fine.

class Worker(object):
	def __init__(self):
		# nothing to see here except the is_placed
		# and of course common methods

		self.is_placed = False
		self.actions = []


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

		# Starting income. Store it in an action, because everything is an action
		starting_resources = {
		'Jewels': 2,
		}

		self.actions.append(StartingIncome(self, starting_resources))

		# Building/resource dictionaries
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

		# Set the Financier's trade actions
		self.actions.append(TradeAction('Jewels',1,'Gears',1))
		self.actions.append(TradeAction('Jewels',2,'Widgets',1))
		self.actions.append(TradeAction('Jewels',2,'Essence',1))


class Blacksmith(Worker):
	def __init__(self):
		# set the name and all the resource combinations
		Worker.__init__(self)
		self.name = 'Blacksmith'

		# Starting income. Store it in an action, because everything is an action
		starting_resources = {
		'Jewels': 1,
		'Gears': 3,
		}

		self.actions.append(StartingIncome(self, starting_resources))


		# Building/resource dictionaries
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

		# Starting income. Store it in an action, because everything is an action
		starting_resources = {
		'Jewels': 1,
		'Widgets': 1,
		}

		self.actions.append(StartingIncome(self, starting_resources))


		# Building/resource dictionaries
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

		# Set the Engineer's trade actions
		self.actions.append(TradeAction('Widgets',1,'Gears',1))


class Alchemist(Worker):
	def __init__(self):
		# set the name and all the resource combinations
		Worker.__init__(self)
		self.name = 'Alchemist'

		# Starting income. Store it in an action, because everything is an action
		starting_resources = {
		'Essence': 2,
		}

		self.actions.append(StartingIncome(self, starting_resources))


		# Building/resource dictionaries
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

		# Set the Alchemist's trade actions
		self.actions.append(TradeAction('Essence',1,'Jewels',1))
		self.actions.append(TradeAction('Essence',1,'Gears',1))
		self.actions.append(TradeAction('Essence',1,'Widgets',1))