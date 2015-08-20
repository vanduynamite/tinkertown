from occupations import *
from buildings import *

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

    def add_starting_resources(self):
    	# this is called during add_starting_occupations
    	# it will cycle through all workers for distinct occupations and add the corresponding starting resources

    	worker_types = []

    	for occupation in self.workers:
    		if type(occupation) not in worker_types:
    			worker_types.append(type(occupation))
	    		self.add_resources(occupation.starting_resources)

    def add_starting_occupations(self, occs, qtys):
    	# occs is a list of occupations to add, qtys is the corresponding quantities

        for i in range(len(occs)):
        	self.workers.extend([occs[i]() for j in range(qtys[i])])

        self.add_starting_resources()

    def list_resources(self):
    	print '%s currently has the following resources: ' % self.name
    	for resource in self.resources:
    		print '   ', self.resources[resource], resource 

    def list_all_workers(self):
    	print '%s currently has the following workers: ' % self.name
    	for worker in self.workers:
    		print '    A %s' % worker.name

    def list_available_workers(self):
        print '%s\'s available workers: ' % self.name
        for worker in self.workers:
            if not(worker.is_placed):
                print '    %s' % worker.name

    def add_resources(self,resource_dictionary):
        for resource in resource_dictionary:
            self.add_resource(resource, resource_dictionary[resource])

    def add_resource(self, resource, amount):
    	self.resources[resource] = self.resources[resource] + amount
















