from game import *

def get_worker(player):
	player.list_available_workers()
	invalid_response = True

	while invalid_response:
		
		worker_num = input('Which worker do you want to use? ')
		
		if isinstance(worker_num, (int)) and worker_num > 0 and worker_num <= len(player.available_workers):
				invalid_response = False
		else:
			print 'Choose a valid worker!'

		
	worker_num -= 1
	print ''
	return player.available_workers[worker_num]

def get_trade_amount(player, resource):
	player.list_resources()
	amount_in = input('How many %s would you like to trade in? ' % resource)
	print ''
	return amount_in

def take_starting_player():
	
	invalid_response = True

	while invalid_response:
		response = input('Starting player is available. Take it? (y/n) ')
		if response == 'y' or response == 'n':
			invalid_response = False
		else:
			print 'Please choose y or n only.'

	print ''

	if response == 'y':
		return True
	else:
		return False