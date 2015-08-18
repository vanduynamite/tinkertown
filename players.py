class Player(object):
    def __init__(self):
        self.resources = {
        'Jewels': 0,
        'Gears': 0,
        'Widgets': 0,
        'Essence': 0,
        }
        
    def list_resources(self):
    	for resource in self.resources:
    		print resource + ': ', self.resources[resource]