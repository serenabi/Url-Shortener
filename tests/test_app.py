import sys
sys.path.append("..")

import unittest
import app
import string, random

letters = string.ascii_lowercase

class testApp(unittest.TestCase):
	def test_toBase36_digits(self):
		for i in range(1, 10):
			result = app.toBase36(i)
			self.assertEqual(result, str(i))

	def test_toBase36_letters(self):		
		for i in range(10, 36):
			result = app.toBase36(i)
			self.assertEqual(result, letters[i-10])

	def test_toBase10_digits(self):
		for i in range(1, 10):
			result = app.toBase10(str(i))
			self.assertEqual(result, i)

	def test_toBase10_letters(self):
		nums = [n for n in range(10, 36)]
		for letter, num in zip(letters, nums):
			result = app.toBase10(letter)
			self.assertEqual(result, num)

	def test_toBase36_random10Strings_fromFirstThousand(self):
		for i in range(10):
			randNum = random.randint(36, 1000)
			base36_conversion = app.toBase36(randNum)
			base10_conversion = app.toBase10(base36_conversion)
			self.assertEqual(base10_conversion, randNum)

	def test_toBase36_random10Strings_fromFirstMillion(self):
		for i in range(10):
			randNum = random.randint(1000, 1000000)
			base36_conversion = app.toBase36(randNum)
			base10_conversion = app.toBase10(base36_conversion)
			self.assertEqual(base10_conversion, randNum)
	
	def test_toBase36_random10Strings_fromFirstTrillion(self):
		for i in range(10):
			randNum = random.randint(1000000, 1000000000000)
			base36_conversion = app.toBase36(randNum)
			base10_conversion = app.toBase10(base36_conversion)
			self.assertEqual(base10_conversion, randNum)