from occupations import *
import sys


class Player(object):
    def __init__(self):
    	# start each player off with no resources and a blank set of workers

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
	    		for resource in occupation.starting_resources:
	    			self.add_resource(resource, occupation.starting_resources[resource])

    def add_starting_occupations(self, occs, qtys):
    	# occs is a list of occupations to add, qtys is the corresponding quantities

        for i in range(len(occs)):
        	self.workers.extend([occs[i]() for j in range(qtys[i])])

        self.add_starting_resources()

    def list_resources(self):
    	for resource in self.resources:
    		print resource + ': ', self.resources[resource]

    def list_workers(self):
    	for worker in self.workers:
    		print worker.name

    def add_resource(self, resource, amount):
    	self.resources[resource] = self.resources[resource] + amount



