import os

shutdown = input("Do you want to shut down the computer? (yes / no): ") 

if shutdown == 'no': 
	exit() 
else: 
	os.system("shutdown /s /t 1") 
