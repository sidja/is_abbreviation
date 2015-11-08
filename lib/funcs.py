
from utils import sanitise
from utils import abbv_split
from utils import lng_form_split
from utils import longform_full_split
from tqdm import *

import itertools

def is_simple(abbreviation, longform):
	'''
		Checks if an abbreviation belongs to category type 'simple'

	'''

	temp =""
	result = False

	## 
	## 	Sanitise abbreviation
	## 	Clean up non letter charcters from string
	## 	Ex 		: "RADIUS"
	## 	Output	: remote authentication dial in user service
	##
	abbreviation = sanitise(abbreviation,"abbv")

	##
	## 	Longform
	## 	Add first letters of long form into a list
	##
	lf = [ i[0].lower() for i in longform.split()]


	##
	## 	Append list items into a temp variable
	##
	for i in lf:
		temp+=i


	##
	## 	Compare 
	##
	if temp == abbreviation and len(temp) == len(abbreviation):

		result = True

	
	return result




def is_complex(abbreviation, longform):
	'''
		Checks if an abbreviation belongs to category type 'complex'

	'''

	result= False

	## 	Santise abbreviation
	## 	
	abbreviation = sanitise(abbreviation,"abbv")

	## Santise longform 
	##
	longform = sanitise(longform,"longform")

	
	## 	Split abbreviation sting into a list 
	## 	with all possible linear combinations with only unique elements
	##
	##	Ex 		: 	"TexMex"
	##
	## 	Output	:	['e', 'ex', 'exm', 'exme', 'exmex', 'm', 'me', 'mex', 't',
	## 				 'te', 'tex', 'texm', 'texme', 'x', 'xm', 'xme', 'xmex']
	
	abbv_list = abbv_split(abbreviation)

	
	
	## 	Change longform string into into a list split
	##	into lenghtwise increments
	##
	##	Ex  : "Texas Mexico"
	##  ['T', 'Te', 'Tex', 'Texa', 'Texas', 'M', 
	## 	'Me', 'Mex', 'Mexi', 'Mexic', 'Mexico']

	
	longform_list = lng_form_split(longform)

	
	
	##
	##	Create an intersection of both lists
	##

	intersection = list(set(abbv_list).intersection(longform_list))

	

	##  Interate through all possible combinations from the intersection 	
	 ##  Compare each combiation with sanitised abberviation 
	  ##  If value exits break and return true

	for L in range(0, len(intersection)+1):
		for subset in itertools.combinations(intersection, L):
			
			l=""
			for i in subset:
				
				l+=i

			
			
			if len(l) == len(abbreviation) and l == abbreviation:
				
				result = True 
				break

	if result == False:
		for L in range(0, len(intersection)+1):
			for subset in itertools.permutations(intersection, L):
				
				l=""
				for i in subset:
					
					l+=i

				
				
				if len(l) == len(abbreviation) and l == abbreviation:
					
					result = True 
					break


	return result





def is_substring(abbreviation, longform):
	'''
		Checks if an abbreviation belongs to category type 'substring'

	'''

	result= False

	## 	Sanitise abbreviation
	## 	
	abbreviation = sanitise(abbreviation,"abbv")

	## Sanitise longform 
	##
	longform = sanitise(longform,"longform")

	
	## 	Split abbreviation sting into a list 
	## 	with all possible linear combinations with only unique elements
	##
	##	Ex : "TexMex"
	## 	['T', 'e', 'x', 'M', 'e', 'x', 'Te', 'ex', 'xM', 'Me',
	## 	'ex', 'Tex', 'exM', 'xMe', 'Mex', 'TexM', 'exMe', 'xMex', 
	## 	'TexMe', 'exMex']
	##
	abbv_list = abbv_split(abbreviation)

	

	## 	Change longform string into into a list split
	##	into lenghtwise increments from the original
	##
	##	Ex  : "Texas Mexico"
	##  ['T', 'Te', 'Tex', 'Texa', 'Texas', 'M', 
	## 	'Me', 'Mex', 'Mexi', 'Mexic', 'Mexico']

	longform_list = longform_full_split(longform)

	#print longform_list


	##
	##	Create an intersection of both lists
	##

	intersection = list(set(abbv_list).intersection(longform_list))

	

	##  Interate through all possible permuatations from the intersection 	
	 ##  Compare each permuatation with sanitised abberviation 
	  ##  If value exits break and return true


	
	for L in range(0, len(intersection)+1):
		for subset in itertools.combinations(intersection, L):
			
			l=""
			for i in subset:
				
				l+=i

			
			
			if len(l) == len(abbreviation) and l == abbreviation:
				
				result = True 
				break


	if result == False:
		for L in tqdm(range(0, len(intersection)+1)):
			for subset in tqdm(itertools.permutations(intersection, L)):
				
				l=""
				for i in subset:
					
					l+=i

				
				
				if len(l) == len(abbreviation) and l == abbreviation:
					
					result = True 
					break





	return result


