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

def get_starting_player(game):

	player_list = []

	for player_name in game.players:
		player_list.append(player_name)

	for i in range(len(player_list)):
		print '%s - %s' % (str(i+1), player_list[i])

	invalid_response = True

	while invalid_response:
		player_num = input('Who is the starting player (number)? ')

		if type(player_num) == int:
			if player_num > 0 and player_num <= len(player_list)+1:
				invalid_response = False
			else:
				print 'Please enter a number between 1 and %s' % len(player_list)+1

		else:
			print 'That\'s not a number! Please enter a number between 1 and %s' % game.num_players

	print ''

	return player_list[player_num - 1]

def get_next_player(game):

	player_list = []

	for player_name in game.players:
		if player_name not in game.turn_order:
			player_list.append(player_name)

	if len(player_list) == 1:
		return player_list[0]
	else:

		for i in range(len(player_list)):
			print '%s - %s' % (str(i+1), player_list[i])

		invalid_response = True

		while invalid_response:
			player_num = input('Who is the next player (number)? ')

			if type(player_num) == int:
				if player_num > 0 and player_num <= len(player_list)+1:
					invalid_response = False
				else:
					print 'Please enter a number between 1 and %s' % len(player_list)+1

			else:
				print 'That\'s not a number! Please enter a number between 1 and %s' % game.num_players

		print ''

		return player_list[player_num - 1]