#!/usr/bin/env python
import socket
import subprocess
import sys
from datetime import datetime

# Clear the screen
#subprocess.call('clear', shell=True)

# Ask for input
#remoteServer    = raw_input("Enter a remote host to scan: ")
#remoteServerIP  = socket.gethostbyname(remoteServer)

# Print a nice banner with information on which host we are about to scan

# Check what time the scan started
#t1 = datetime.now()

# Using the range function to specify ports (here it will scans all ports between 1 and 1024)

# We also put in some error handling for catching errors

def get_alive():
    remoteServerIPHEAD  = "192.168.12."
    result_str = ""

    try:
        for ip in range(105,130):
            remoteServerIP_str = remoteServerIPHEAD + str(ip)
            remoteServerIP  = socket.gethostbyname(remoteServerIP_str)
            print "-" * 60
            print "Please wait, scanning remote host", remoteServerIP_str
            print "-" * 60
            for port in range(21,23):  
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(1)
                    try:
                       result = sock.connect_ex((remoteServerIP, port))
                    except socket.timeout:
                        print "time out "
                    else:
                        if result == 0:
                          print "Port {}: 	 Open".format(port)
                          result_str += "{} is alive. \n".format(remoteServerIP_str)
                        sock.close()

    except KeyboardInterrupt:
        print "You pressed Ctrl+C"
        sys.exit()

    except socket.gaierror:
        print 'Hostname could not be resolved. Exiting'
        sys.exit()

    except socket.error:
        print "Couldn't connect to server"
        sys.exit()

    return result_str
hello = get_alive()
print hello

# Checking the time again
#t2 = datetime.now()

# Calculates the difference of time, to see how long it took to run the script
#total =  t2 - t1

# Printing the information to screen
#print 'Scanning Completed in: ', total
