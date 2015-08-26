from game import *

class Machine(object):
	def __init__(self, game):

		self.game = game
		self.status = 'supply' #supply, sale, owned, gone
		self.type = 'unknown'
		self.place_actions = []
		self.passive_actions = []
		self.trigger_actions = []

	def purchase(self, player, worker):
		self.owner = player
		self.status = 'owned'
		negative_cost = {}

		for resource, qty in self.cost.items():
			negative_cost[resource] = -1*qty

		player.add_resources(negative_cost)

		self.add_actions(player)

		self.game.check_machines()

	def list_price(self):
		cost_string = ''
		for resource, qty in self.cost.items():
			if len(cost_string) != 0:
				cost_string = cost_string + ' and '
			cost_string = cost_string + '%s %s' % (qty, resource)

		return cost_string

	def adjust_cost(self, worker):
		for action in worker.trigger_actions:
			if action.trigger == 'buy small machine':
				self.cost = action.execute(self.cost)

	def reset_cost(self):
		self.cost = {
		'Jewels': self.game.round + 1,
		'Gears': self.game.round + 1,
		}

class SmallMachine(Machine):
	def __init__(self, game):
		Machine.__init__(self, game)
		self.type = 'small'

		self.cost = {
		'Jewels': self.game.round + 1,
		'Gears': self.game.round + 1,
		}

		self.power = 2

class SmallIncomeMachine(SmallMachine):
	def __init__(self, game, resource, qty):
		SmallMachine.__init__(self, game)
		self.resource = resource
		self.qty = qty
		self.name = '%s %s income' % (qty, resource)

	def add_actions(self, player):
		self.trigger_actions.append(MachineIncome(player, self.resource, self.qty))
		self.trigger_actions.append(MachinePower(player, self.power))

class SmallPowerMachine(SmallMachine):
	def __init__(self, game):
		SmallMachine.__init__(self, game)

		self.power = 5
		self.name = '%s Power' % self.power

	def add_actions(self, player):
		self.trigger_actions.append(MachinePower(player, self.power))