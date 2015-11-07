import re
# from tqdm import *
# import itertools


def sanitise(string,option):
	'''
		Santises input string - returns a string

		a. Option "abbv" 	: 	Removes all non letter charcters 
								from input string
		b. Option "longform":	Same as above but exlcudes spaces

	'''

	temp = ""

	string = string.lower()

	if option == "abbv":
		regex = re.compile('[^a-zA-Z]')

	elif option == "longform":
		regex = re.compile('[^a-zA-Z]\s')

	string = regex.sub('', string)

	return string


# print sanitise("Remote Authentication Dial In User Service","longform")





def abbv_split(a):
	'''	
		Splits word into a sorted list of all possible linear combinations
		with unique elements

		Ex 		: 	"TexMex"

		Output	:	['e', 'ex', 'exm', 'exme', 'exmex', 'm', 'me', 'mex', 't',
					 'te', 'tex', 'texm', 'texme', 'x', 'xm', 'xme', 'xmex']


	'''

	r = len(a)

	l = []

	for j in range(1,r):
		diff = j



		for i in range(r+1):
			x=0
			y=i
			count=0

			while count<=r:
				
				if y-x == diff:
					#print "x:",x, " y:",y
					#print a[x:y]
					l.append(a[x:y].lower())
				x+=1
				count+=1
			
			#print "count:", count, " x:", x, " y:",y	



	return sorted(list(set(l))) 


# a="TexMex"
# print abbv_split(a)





def lng_form_split(lng_form):
	'''
	Splits sting into a sorted list of strings consisting of
 	linear increments from the original string
	

	Ex 		:	"Texas Mexico"

	Output	:	['m', 'me', 'mex', 'mexi', 'mexic', 'mexico', 't', 'te', 
				'tex', 'texa', 'texas']
	'''



	lngfrm_words = lng_form.split()

	lng_list = []

	


	for a in lngfrm_words:
		



		#l = []
		st = ""
		for i in a:
			st = st+ i
			lng_list.append(st.lower())


		
		
	return sorted(list(set(lng_list)))


# lng_form = "Texas Mexico"

# print lng_form_split(lng_form)


def longform_full_split(a):

	'''
		Splits string into a sorted list of all possible left to 
		right letter combinations
		

		Ex 		: "San Franciso"
		
		Output 	: ['a', 'an', 'anc', 'anci', 'ancis', 'ancisc', 'ancisco', 'c', 'ci', 'cis', 
				'cisc', 'cisco', 'co','f', 'fr', 'fra', 'fran', 'franc', 'franci', 'francis',
				'francisc', 'i', 'is', 'isc', 'isco', 'n','nc', 'nci', 'ncis', 'ncisc', 
				'ncisco', 'o', 'r', 'ra', 'ran', 'ranc', 'ranci', 'rancis', 'rancisc',
				'rancisco', 's', 'sa', 'sc', 'sco']

	'''


	lngfrm_words = a.split()

	lng_list = []

	for a in lngfrm_words:

		r = len(a)

		#l = []

		for j in range(1,r):
			diff = j



			for i in range(r+1):
				x=0
				y=i
				count=0

				while count<=r:
					
					if y-x == diff:
						#print "x:",x, " y:",y
						#print a[x:y]
						lng_list.append(a[x:y].lower())
					x+=1
					count+=1
				
				#print "count:", count, " x:", x, " y:",y	


	return sorted(list(set(lng_list)))



# a="San Francisco"

# print longform_full_split(a)


# def iterate_combination(intersection,abbreviation):

# 	for L in tqdm(range(0, len(intersection)+1)):
# 			for subset in itertools.combinations(intersection, L):
# 				#print(subset)
# 				l=""
# 				for i in subset:
# 					#print i
# 					l+=i

# 				# if len(l) == len(abbreviation):
# 				# 	print l
				
# 				if len(l) == len(abbreviation) and l == abbreviation:
# 					#print l
# 					return True
# 					break

# 	return False


# def iterate_permutation(intersection,abbreviation):

# 	for L in tqdm(range(0, len(intersection)+1)):
# 			for subset in itertools.permutations(intersection, L):
# 				#print(subset)
# 				l=""
# 				for i in subset:
# 					#print i
# 					l+=i

# 				# if len(l) == len(abbreviation):
# 				# 	print l
				
# 				if len(l) == len(abbreviation) and l == abbreviation:
# 					#print l
# 					return True
# 					break

# 	return False