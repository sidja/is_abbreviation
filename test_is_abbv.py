from is_abbv import is_abbreviation
import time


def check_abbv(abbreviation, longform):
	
	start_time = time.time()

	
	print abbreviation, longform ,"---> ",is_abbreviation(abbreviation, longform)
	
	print("--- %s seconds ---" % (time.time() - start_time))
	print



check_abbv('AusPost','Australia Post')
check_abbv("RADIUS", "Remote Authentication Dial In User Service")
check_abbv("AusPost", "Australia Post")
check_abbv("FedEx", "Federal Express")
check_abbv("ragnat", "Teragen International")
check_abbv("cisco", "San Francisco")
check_abbv("sonposa", "sonhaypohemsa")
check_abbv("FoxTel", "Fox Television")
check_abbv("CommBank", "Commonwealth Bank")

check_abbv("Gestapo", "Geheime Staats Polizei")
check_abbv("Comintern", "Communist International")