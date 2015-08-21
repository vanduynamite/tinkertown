from players import *
from workers import *
from buildings import *
from actions import *
from machines import *

class Game(object):
	def __init__(self):
		# self.num_players = input('Number of players? ')
		self.workers_per_occupation = 4
		self.num_rounds = 4

		self.num_players = 0
		self.players = {}
		self.buildings = {}

	def create_players(self, players):
		
		for name, occupations in players.items():

			self.players[name] = Player(name)

			player = self.players[name]

			player.add_starting_occupations(occupations,[self.workers_per_occupation for i in occupations])

			self.check_actions(player)

			# based on the occupations added, get their starting resources
			for action in player.start_game_actions:
				action.start(player)

			self.check_actions(player)


	def create_buildings(self):
		self.buildings['Bank'] = Bank(self.num_players)
		self.buildings['Forge'] = Forge(self.num_players)
		self.buildings['Workshop'] = Workshop(self.num_players)
		self.buildings['Townhall'] = TownHall(self.num_players)


	def create_market(self):
		pass

	def create_townhall_cards(self):
		pass

	def set_up_game(self, players):
		self.num_players = len(players)

		self.create_buildings()
		self.create_market()
		self.create_townhall_cards()

		self.create_players(players)

	def check_actions(self, player):
		# this method will be called throughout the game to make sure the player has the correct actions

		player.start_game_actions = []
		player.place_actions = []
		player.passive_actions = []
		player.trigger_actions = []

		player.actions = {
		'Start Game' : player.start_game_actions,
		'Place Worker' : player.start_game_actions,
		'Passive Action' : player.start_game_actions,
		'Triggered Actions' : player.start_game_actions,
		}

		# check the occupations first
		for worker in player.workers:
			for action_type, player_action_set in player.actions.items():
				for worker_action in worker.actions[action_type]:

					action_name = worker_action.name

					if action_name not in [action.name for action in player_action_set]:
							player_action_set.append(worker_action)


		# then check all the buildings for available spots
		for name, building in self.buildings.items():
			if building.is_available():
				player.place_actions.append(BuildingAction(building, player))


		# and then check the machines
		"""Not done yet, obviously. Machines don't exist yet!"""

	def list_players(self):
		for player_name in self.players:
			print player_name

	def list_available_buildings(self):
		for name, building in self.buildings.items():
			if building.is_available():
				print '    The %s is available' % name