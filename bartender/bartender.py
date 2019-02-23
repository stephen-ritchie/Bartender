

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
import logging
from pprint import pprint
import time

FLOW_RATE = 60


class Bartender:
	"""
	"""

	def __init__(self):
		self.drink_list = self._load_drink_list()
		self.pump_config = self._load_pump_config()

		
	def _load_drink_list(self):
		"""
		"""

		filename = "/Users/Stephen/projects/Bartender/bartender/drinklist.json"
		with open(filename) as f:
			data = json.load(f)
		return data


	def _load_pump_config(self):
		"""
		"""

		filename = "/Users/Stephen/projects/Bartender/bartender/pump_config.json"
		with open(filename) as f:
			data = json.load(f)
		return data


	def _get_ingredients(self, drink):
		"""Gets ingredients for the provided drink.

		Args:
			drink: Name of drink
		Returns:
			Ingredients and their amounts (mL) as JSON object.
		"""

		try:
			return self.drink_list[drink]["ingredients"]
		except:
			logger.error("Could not find ingredients for:%s" % drink)
			return None


	def _mililiters_to_seconds(self, amount):
		"""Convert from mililiters to seconds based on pump flow rate.

		Args:
			amount:
		Returns:
			Number of seconds to achieve amount at configured flow rate
		"""

		return 1

	def _get_pin(self, ingredient):
		"""Searches pump configuration for pin associated with provided ingredient.

		Args:
			ingredient: item to find associated pin for in config
		Returns:
			The pin number - None if the pin cannot be found
		"""

		pin = None
		for pump,info in self.pump_config.items():
			if info['value'] == ingredient:
				pin = info['pin']

		return pin


	def _pour(self, wait_time, pin, ingredient=None):
		"""Uses GPIO to activate provided pin on Raspberry Pi.

		Args:
			wait_time: time in seconds
			pin: pin number on raspberry pi
			ingredient (optional): provides extra debugging info to log
		Returns:
			None
		"""

		logger.debug("Pin %s (%s) being activated for %s second(s)" % (pin, ingredient, wait_time))
		time.sleep(wait_time)


	def make_drink(self, drink_name):
		"""
		"""

		logger.info("Making a %s" % drink_name)

		# Retrieve required ingredients for drink
		ingredients = self._get_ingredients(drink_name)
		if ingredients is None:
			logger.error("Could not pour a %s because the ingredients could not be found" % drink_name)
			return

		# Iterate through each ingredient and turn on the corresponding pump for
		# the correct amount of time.
		for ingredient, amount in ingredients.items():

			pour_time = self._mililiters_to_seconds(amount)

			pin = self._get_pin(ingredient)
			if pin is None:
				logger.error("Could not find pin for %s" % ingredient)

			self._pour(pour_time, pin, ingredient)

		logger.debug("Done making a %s" % drink_name)


if __name__ == "__main__":
	logging.basicConfig(filename='../run.log',level=logging.DEBUG)
	logger = logging.getLogger(__name__)

	bartender = Bartender()
	bartender.make_drink("BourbonAndCoke")

