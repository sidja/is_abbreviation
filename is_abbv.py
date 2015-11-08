
import os
from optparse import OptionParser 
import sys

from lib.funcs import is_simple, is_complex, is_substring
from lib.utils import prettify_result
import unittest    
from lib.tests import *



def is_abbreviation(abbreviation, longform):
	
	category = None 
	outcome = False

	if len(abbreviation)!=0 and len(longform)!=0:
	
		if is_simple(abbreviation, longform):
			category = 'simple'
			outcome = True

		elif is_complex(abbreviation, longform):
			category = 'complex'
			outcome = True

		elif is_substring(abbreviation, longform):
			category = 'substring'
			outcome = True

	
	return outcome, category






def main(argv):
	'''
			Commandline menu function

	'''

	description = "Utility function to check abbreviation against their longforms"


	parser = OptionParser(description=description,
				usage='usage: %prog [OPTIONS]  <abbreviation> <longform>')
	
	parser.add_option("-m",  dest="manual",
    	help="check abbreviation manually \t\t\t\t\t ex: 'is_abbv.py -m <abbreviation> <longform>' ",
    	type="string",nargs=2)
	
	(options, args) = parser.parse_args()
	
	if options.manual:
		
		prettify_result(is_abbreviation(options.manual[0],options.manual[1]))
		
	

	if len(sys.argv) == 1:
		parser.parse_args(['--help'])

if __name__ == "__main__":
   main(sys.argv[1:])
