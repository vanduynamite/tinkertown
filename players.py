from game import *

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
        self.actions = []



    def add_starting_occupations(self, occs, qtys):
    	# occs is a list of occupations to add, qtys is the corresponding quantities

        for i in range(len(occs)):
        	self.workers.extend([occs[i]() for j in range(qtys[i])])




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
        
        i = 1
        
        for worker in self.workers:
            if not(worker.is_placed):
                print '    %s - %s' % (str(i), worker.name)
                i += 1

        print ''

    def list_actions(self):
        # list the actions this player has

        print '%s\'s actions:' % self.name

        for action in self.actions:
            print '    %s (occurs on %s)' % (action.name, action.trigger)

        print ''
















