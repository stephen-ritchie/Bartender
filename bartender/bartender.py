

# Functions I need to make
# Public
# make_drink(name)
# clean()
#
# Private
# load_drink_list()
# load_pump_config()
# record_drink(name, person?)
#
# pour(pin, time)

import json
from pprint import pprint


class Bartender:

	def __init__(self):
		self.load_drink_list()
		

	def load_drink_list(self):
		filename = "bartender/drinklist.json"
		with open(filename) as f:
			data = json.load(f)
		pprint(data)





app = Bartender()