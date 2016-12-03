#===================================================================================
#This program is to generate extended ipoib
#traffic via ping and other methods   
#
#
#
#===================================================================================
#!/usr/bin/python
#import modules needed for script
timeimport sys
import os
import subprocess
import pickle
import time

# opens and reads host file




# loop for extended pings
for h in host:
	os.system("ping -i 0.2 -t 3 -c 1000 -s 256 h")
    os.system("ping -i 0.2 -t 3 -c 1000 -s 512 h")
	os.system("ping -i 0.2 -t 3 -c 1000 -s 1024 h")
	os.system("ping -i 0.2 -t 3 -c 1000 -s 2048 h")
	os.system("ping -i 0.2 -t 3 -c 1000 -s 4096 h")
	os.system("ping -i 0.2 -t 3 -c 1000 -s 8096 h")
	os.system("ping -i 0.2 -t 3 -c 1000 -s 24576 h")
    os.system("ping -i 0.2 -t 3 -c 1000 -s 49512 h")
		

     

