import unittest
from fizzbuzz import *

class TestDojo(unittest.TestCase):
	def setUp(self):
		self.fizzbuzz = FizzBuzz()

	def test_when_number_is_multiple_of_3_should_return_Fizz(self):
		assert self.fizzbuzz.show(3) == 'Fizz'
		assert self.fizzbuzz.show(9) == 'Fizz'

	def test_when_number_is_multiple_of_5_should_return_Buzz(self):
		assert self.fizzbuzz.show(5) == 'Buzz'
		assert self.fizzbuzz.show(10) == 'Buzz'

	def test_when_number_is_multiple_of_15_should_return_FizzBuzz(self):
		assert self.fizzbuzz.show(15) == 'FizzBuzz'
		assert self.fizzbuzz.show(30) == 'FizzBuzz'

	def test_when_number_is_not_multiple_of_3_or_5_should_return_itself(self):
		assert self.fizzbuzz.show(2) == 2
		assert self.fizzbuzz.show(4) == 4
