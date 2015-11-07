
from utils import sanitise
from utils import abbv_split
from utils import lng_form_split
from utils import longform_full_split
from tqdm import *

import itertools

def is_simple(abbreviation, longform):

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
	##
	##
	lf = [ i[0].lower() for i in longform.split()]



	## Append list items into a temp variable
	for i in lf:
		temp+=i



	## Compare 
	if temp == abbreviation and len(temp) == len(abbreviation):

		result = True

	
	return result



#print is_simple("RADIUS", "Remote Authentication Dial In User Service")


def is_complex(abbreviation, longform):

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

	# print abbv_list
	
	## 	Change longform string into into a list split
	##	into lenghtwise increments
	##
	##	Ex  : "Texas Mexico"
	##  ['T', 'Te', 'Tex', 'Texa', 'Texas', 'M', 
	## 	'Me', 'Mex', 'Mexi', 'Mexic', 'Mexico']

	
	longform_list = lng_form_split(longform)

	# print longform_list
	
	##
	##	Create an intersection of both lists
	##

	intersection = list(set(abbv_list).intersection(longform_list))

	# print intersection

	##  Interate through all possible combinations from the intersection 	
	 ##  Compare each combiation with sanitised abberviation 
	  ##  If value exits break and return true

	for L in range(0, len(intersection)+1):
		for subset in itertools.combinations(intersection, L):
			#print(subset)
			l=""
			for i in subset:
				#print i
				l+=i

			#print l
			
			if len(l) == len(abbreviation) and l == abbreviation:
				#print l
				result = True 
				break

	if result == False:
		for L in range(0, len(intersection)+1):
			for subset in itertools.permutations(intersection, L):
				#print(subset)
				l=""
				for i in subset:
					#print i
					l+=i

				# if len(l) == len(abbreviation):
				# 	print l
				
				if len(l) == len(abbreviation) and l == abbreviation:
					#print l
					result = True 
					break


	return result


# print is_complex("AusPost", "Australia Post")
# print is_complex("FedEx", "Federal Express")

#print is_complex("sonposa", "sonhaypohemsa")
# print is_complex("FoxTel", "Fox Television")




def is_substring(abbreviation, longform):

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

	# print abbv_list

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

	#print intersection

	##  Interate through all possible permuatations from the intersection 	
	 ##  Compare each permuatation with sanitised abberviation 
	  ##  If value exits break and return true


	
	for L in range(0, len(intersection)+1):
		for subset in itertools.combinations(intersection, L):
			#print(subset)
			l=""
			for i in subset:
				#print i
				l+=i

			# if len(l) == len(abbreviation):
			# 	print l
			
			if len(l) == len(abbreviation) and l == abbreviation:
				#print l
				result = True 
				break


	if result == False:
		for L in tqdm(range(0, len(intersection)+1)):
			for subset in tqdm(itertools.permutations(intersection, L)):
				#print(subset)
				l=""
				for i in subset:
					#print i
					l+=i

				# if len(l) == len(abbreviation):
				# 	print l
				
				if len(l) == len(abbreviation) and l == abbreviation:
					#print l
					result = True 
					break





	return result


# print is_substring("ragnat", "Teragen International")
# print is_substring("cisco", "San Francisco")
# print is_substring("sonposa", "sonhaypohemsa")

