

from funcs import is_simple, is_complex, is_substring


def is_abbreviation(abbreviation, longform):
	
	category = None 
	outcome = False

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



# print is_abbreviation('AusPost','Australia Post')
# print is_abbreviation("RADIUS", "Remote Authentication Dial In User Service")
# print is_abbreviation("AusPost", "Australia Post")
# print is_abbreviation("FedEx", "Federal Express")
# print is_abbreviation("ragnat", "Teragen International")
# print is_abbreviation("cisco", "San Francisco")
# print is_abbreviation("sonposa", "sonhaypohemsa")
# print is_abbreviation("FoxTel", "Fox Television")
# print is_abbreviation("CommBank", "Commonwealth Bank")
# print is_abbreviation("AmEx", "American Express")
# print is_abbreviation("TexMex", "Texas Mexico")
# print is_abbreviation("Gestapo", "Geheime Staats Polizei")
# print is_abbreviation("Comintern", "Communist International")
# print is_abbreviation("Wifi", "Wirelss Fidility")
# print is_abbreviation("Hifi", "High Fidility ")
# print is_abbreviation("B.Comm","Bachelor of Commerce")

