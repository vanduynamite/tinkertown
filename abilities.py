from players import *
from workers import *
from buildings import *
from machines import *

"""Will have all sorts of different abilities in here to reference! That way each ability can be modified independently of the rest of the program. I mean, that's the reason for all of this, right..."""

class Ability(object):
	def __init__(self):
		self.name = 'unknown ability'
		self.trigger = 'unknown'


class StartingIncome(Ability):
	def __init__(self, occupation, resources):
		Ability.__init__(self)
		self.name = '%s\'s starting income' % occupation.name
		self.trigger = 'trigger_game_start'

		self.resource_transaction = resources

	def start(self, player):
		print '---Ability: Starting Income---'
		print '   %s got the %s' % (player.name, self.name)
		print ''
		player.add_resources(self.resource_transaction)


class TradeAbility(Ability):
	def __init__(self, resource_in, resource_in_amt, resource_out, resource_out_amt):
		# Generic trade transaction
		# Specify which resource comes in and how many you need
		# and specify what and how much comes out!

		Ability.__init__(self)
		self.name = '%s %s for %s %s' % (str(resource_in_amt), str(resource_in), str(resource_out_amt), str(resource_out))
		self.trigger = 'trigger_trade'

		self.resource_in = resource_in
		self.resource_out = resource_out

		# Use this in the actual transaction below
		self.transaction = {
		resource_in : resource_in_amt,
		resource_out : resource_out_amt,
		}

	def trade(self, player, amount_in):
		# First check the amount available to make sure they're not asking for too much
		amount_available = player.resources[self.resource_in]

		if amount_in > amount_available:
			# If not, delived the bad news
			print '%s does not have enough %s!' % (player.name, self.resource_in),
			print '(requested: %s, available: %s)' % (str(amount_in), str(amount_available))
			print ''
			return False
		else:
			# Get a corrected amount in case they want to trade some incorrect ratio
			corrected_amount_in = int(amount_in/self.transaction[self.resource_in])*self.transaction[self.resource_in]

			# Calculate the amount out
			amount_out = amount_in/self.transaction[self.resource_in]*self.transaction[self.resource_out]

			# build a resource dictionary and perform the transaction for the player
			resource_transaction = {
			self.resource_in : -1*corrected_amount_in,
			self.resource_out : amount_out
			}

			player.add_resources(resource_transaction)

			# And send confirmation!
			print '---Ability: Trade---'
			print '   %s traded %s %s for %s %s' % (player.name, str(corrected_amount_in), self.resource_in, str(amount_out), self.resource_out)
			print ''


			return True

class IncomeAbility(Ability):
	def __init__(self):
		Ability.__init__(self)
		self.name = 'unknown income ability'
		self.trigger = 'trigger_round_start'

		"""Do this one next"""

class PassiveAbility(Ability):
	def __init__(self):
		Ability.__init__(self)
		self.name = 'unknown passive ability'

class ActiveAbility(Ability):
	def __init__(self):
		Ability.__init__(self)
		self.name = 'unknown active ability'

class EndgameAbility(Ability):
	def __init__(self):
		Ability.__init__(self)
		self.name = 'unknown endgame ability'


