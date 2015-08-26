from game import *

class Machine(object):
	def __init__(self):

		self.status = 'not available' #not available, owned, for sale
		self.type = 'unknown'
		self.place_actions = []
		self.passive_actions = []
		self.trigger_actions = []

	def purchase(self, player):
		self.owner = player

		for resource, qty in self.cost.items():
			negative_cost[resource] = -1*qty

		player.add_resources(negative_cost)

		self.add_actions(player)

class SmallMachine(Machine):
	def __init__(self, game):
		Machine.__init__(self)
		self.type = 'small'

		self.cost = {
		'Jewels': game.round + 1,
		'Gears': game.round + 1,
		}

		self.power = 2

class SmallIncomeMachine(SmallMachine):
	def __init__(self, game, resource, qty):
		SmallMachine.__init__(self, game)
		self.resource = resource
		self.qty = qty

	def add_actions(self, player):
		self.trigger_actions.append(MachineIncome(player, self.resource, self.qty))
		self.trigger_actions.append(MachinePower(player, self.power))

class SmallPowerMachine(SmallMachine):
	def __init__(self, game):
		SmallMachine.__init__(self, game)

		self.power = 5

	def add_actions(self, player):
		self.trigger_actions.append(MachinePower(player, self.power))