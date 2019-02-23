import unittest
from bartender import bartender

class BartenderTest(unittest.TestCase):
	def setUp(self):
		print("hello")
		driver = bartender.Bartender()
		assertNotNull(bartender)

	def test(self):
		print("hello")

if __name__ == '__main__':
    unittest.main()
