#!/bin/python3

import socket
import sys
from datetime import datetime

#Check to make sure only 2 arguments passed in
if len(sys.argv) == 2:
    #Accounts for hostname instead of IP address
    host = socket.gethostbyname(sys.argv[1]) 
else:
    print('Invalid syntax. Proper syntax - python3 scanner.py <ip>')
    
print('\/'*20)
print('Scanning Target: {}'.format(host))
print('Scan started at {}'.format(str(datetime.now())))
print('\/'*20)


ports = [20,21,22,23,25,53,80,88,443,445,389,3389,8080]

try:
    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((host,port))
        if result == 0:
            print('Port {} - open'.format(port))
        else:
            print('Port {} - closed'.format(port))
        s.close()
        
except KeyboardInterrupt:
    print('\nExiting program - user interrupt')
    sys.exit()
    
except socket.gaierror:
    print('Could not resolve hostname {}'.format(host))
    sys.exit()
    
except socket.error:
    print('{} not reachable'.format(host))
    sys.exit()
    
 


