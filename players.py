from workers import *
from buildings import *
from abilities import *
from machines import *

class Player(object):
    def __init__(self, name):
    	# start each player off with no resources and a blank set of workers

    	self.name = name

        self.resources = {
        'Jewels': 0,
        'Gears': 0,
        'Widgets': 0,
        'Essence': 0,
        }

        self.workers = []
        self.abilities = []


    def check_abilities(self):
        # this method will be called throughout the game to make sure the player has the correct abilities

        self.abilities = []

        # check the occupations first
        for worker in self.workers:
            for worker_ability in worker.abilities:
                ability_name = worker_ability.name

                if ability_name not in [ability.name for ability in self.abilities]:
                    self.abilities.append(worker_ability)


        # and then check the machines
        """Not done yet, obviously. Machines don't exist yet!"""

    def add_starting_occupations(self, occs, qtys):
    	# occs is a list of occupations to add, qtys is the corresponding quantities

        for i in range(len(occs)):
        	self.workers.extend([occs[i]() for j in range(qtys[i])])

        # run check_abilities as we've just made a change
        self.check_abilities()

        # then based on the occupations added, get their starting resources
        for ability in self.abilities:
            if ability.trigger == 'trigger_start':
                ability.start(self)




    def add_resources(self,resource_dictionary):
        # takes in a dictionary and adds the resources accordingly
        # it's a dictionary if later more resources are added or removed
        for resource in resource_dictionary:
            self.add_resource(resource, resource_dictionary[resource])

    def add_resource(self, resource, amount):
        # if ever you need to add a single resource of a specific amount
        self.resources[resource] = self.resources[resource] + amount





    def list_resources(self):
        # simply list the resources for this player
    	print '%s currently has the following resources: ' % self.name
    	for resource in self.resources:
    		print '   ', self.resources[resource], resource 
                
        print ''

    def list_all_workers(self):
        # list all workers, whether placed or not
    	print '%s currently has the following workers: ' % self.name
    	for worker in self.workers:
    		print '    %s' % worker.name
                
        print ''

    def list_available_workers(self):
        # list only the unplaced workers
        print '%s\'s available workers: ' % self.name
        for worker in self.workers:
            if not(worker.is_placed):
                print '    %s' % worker.name

        print ''

    def list_abilities(self):
        # list the abilities this player has
        self.check_abilities()

        print '%s\'s abilities:' % self.name

        for ability in self.abilities:
            print '    %s (occurs at %s)' % (ability.name, ability.trigger)

        print ''
















