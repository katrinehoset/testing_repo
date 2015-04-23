import unittest

from pydna import seq_utils

class TestSeqUtils(unittest.TestCase):
	def test_is_codon_correct_good_codon(self):
		codon = 'ATG'
		result = seq_utils.is_codon_correct(codon)
		expected = True
		self.assertEqual(expected, result)
	
	def test_is_codon_correct_bad_codon1(self):
		codon = 'T*G'
		result = seq_utils.is_codon_correct(codon)
		expected = False
		self.assertEqual(expected, result)
	
	def test_is_codon_correct_bad_codon2(self):
		codon = 457.45
		result = seq_utils.is_codon_correct(codon)
		expected = False
		self.assertEqual(expected, result)