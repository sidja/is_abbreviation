from is_abbv import is_abbreviation, prettify_result
import time
import unittest
from lib.funcs import is_simple, is_complex, is_substring
from lib.utils import sanitise, abbv_split, lng_form_split, longform_full_split




class TestisAbbreviationFunctions(unittest.TestCase):


	def test_is_simple(self):
		abbreviation="RADIUS"
		longform="Remote Authentication Dial In User Service"
		assertion=True
		self.assertEqual(is_simple(abbreviation, longform), assertion)
		

	def test_is_complex(self):
		abbreviation="CommBank"
		longform="Commonwealth Bank"
		assertion=True
		self.assertEqual(is_complex(abbreviation, longform), assertion)
		

	def test_is_substring(self):
		abbreviation="cisco"
		longform="San Francisco"
		assertion=True
		self.assertEqual(is_substring(abbreviation, longform), assertion)
		

	def test_santise_abbreviation(self):
		abbreviation="R.A.D.I.U.S"
		option="abbv"
		assertion="radius"
		self.assertEqual(sanitise(abbreviation,option),assertion)
		

	def test_santise_longform(self):
		longform="Remote Authentication Dial In User Service"
		option="longform"
		assertion="remote authentication dial in user service"
		self.assertEqual(sanitise(longform,option),assertion)
		

	def test_abbv_split(self):
		test_input="TexMex"
		assertion=['e', 'ex', 'exm', 'exme', 'exmex', 'm', 'me', 
				'mex', 't', 'te', 'tex', 'texm', 'texme', 'x', 
				'xm', 'xme', 'xmex']
		self.assertEqual(abbv_split(test_input),assertion)
		

	def test_lng_form_split(self):
		test_input="Texas Mexico"
		assertion=['m', 'me', 'mex', 'mexi', 'mexic', 'mexico', 
				't', 'te', 'tex', 'texa', 'texas']

		self.assertEqual(lng_form_split(test_input),assertion)
		

	def test_longform_full_split(self):
		test_input="San Francisco"
		assertion=['a', 'an', 'anc', 'anci', 'ancis', 'ancisc', 'ancisco',
		 	'c', 'ci', 'cis', 'cisc', 'cisco', 'co', 'f', 'fr', 'fra', 'fran', 'franc',
		  	'franci', 'francis', 'francisc', 'i', 'is', 'isc', 'isco', 'n', 'nc',
		  	'nci', 'ncis', 'ncisc', 'ncisco', 'o', 'r', 'ra', 'ran', 'ranc', 'ranci',
		 	'rancis', 'rancisc', 'rancisco', 's', 'sa', 'sc', 'sco']

		self.assertEqual(longform_full_split(test_input),assertion)
		




class TestisAbbreviation(unittest.TestCase):

	def test_simple(self):
		abbreviation="RADIUS"
		longform="Remote Authentication Dial In User Service"
		assertion=(True,'simple')
		self.assertEqual(is_abbreviation(abbreviation, longform),assertion)
		

	def test_complex(self):
		abbreviation='AusPost'
		longform='Australia Post'
		assertion=(True,'complex')
		self.assertEqual(is_abbreviation(abbreviation, longform),assertion)
		

	def test_substring(self):
		abbreviation='cisco'
		longform="San Francisco"
		assertion=(True,'substring')
		self.assertEqual(is_abbreviation(abbreviation, longform),assertion)
		

	def test_failcase(self):
		abbreviation="RIP"
		longform="Wrong"
		assertion=(False, None)
		self.assertEqual(is_abbreviation(abbreviation, longform),assertion)
		
	def test_empty(self):
		abbreviation=""
		longform=""
		assertion=(False, None)
		self.assertEqual(is_abbreviation(abbreviation, longform),assertion)

	def test_prettify_result_positive(self):
		test_input=(True, 'complex')
		self.assertTrue(prettify_result(test_input))

	def test_prettify_result_negative(self):
		test_input=(False, None)
		self.assertTrue(not prettify_result(test_input) )



if __name__ == '__main__':
    unittest.main()