import re


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

					l.append(a[x:y].lower())
				x+=1
				count+=1
			


	return sorted(list(set(l))) 




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
		

		st = ""
		for i in a:
			st = st+ i
			lng_list.append(st.lower())


		
		
	return sorted(list(set(lng_list)))




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

	
		for j in range(1,r):
			diff = j



			for i in range(r+1):
				x=0
				y=i
				count=0

				while count<=r:
					
					if y-x == diff:
						
						lng_list.append(a[x:y].lower())
					x+=1
					count+=1
				

	return sorted(list(set(lng_list)))




def prettify_result(tupl):
	'''
		Prettifies the the is_abbreviation() result 
	'''
	if tupl[0]==False:

		print "\n\tThis is not a valid abbreviation for this longform\t\n"
		
	else:
		print "\n\t This is a valid abbreviation"
		print "\t Category 	:",tupl[1]
		print 
		
	return tupl[0]
