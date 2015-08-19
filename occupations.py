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
    	self.name = 'Financier'
    	self.starting_resources = {
    	'Jewels': 2,
    	}

class Blacksmith(Worker):
	def __init__(self):
		self.name = 'Blacksmith'
		self.starting_resources = {
		'Jewels': 1,
		'Gears': 3,
		}

class Engineer(Worker):
	def __init__(self):
		self.starting_resources = {
		'Jewels': 1,
		'Widgets': 1,
		}

class Alchemist(Worker):
	def __init__(self):
		self.starting_resources = {
		'Essence': 2,
		}