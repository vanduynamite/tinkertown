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

class Financier(Worker):
    def __init__(self):
    	Worker.__init__(self)
    	self.name = 'Financier'
    	self.starting_resources['Jewels'] = 2

    	"""Thinking about replacing the below go_to_bank method with some much more clever thing, like sending buildings and then each worker having a dictionary with a 'resource dictionary' defined for each entry and then just plug-n-chug. Dunno yet"""
    	self.bank_resources = {
    	'Jewels' : 2,
    	}


    def go_to_bank(self,player,bank):
    	if bank.is_available:
    		player.add_resource(,2)
    		bank.use_spot()
    		self.is_placed = True
    		return True
    	else:
    		print 'Bank is full! (from Financier class)'
    		return False


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