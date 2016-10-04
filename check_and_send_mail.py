import mailbox
import time 
import subprocess
import socket
import sys
import os
import socket
import fcntl
import struct
import datetime
from email.mime.text import MIMEText
def get_interface_ip(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s',
                                ifname[:15]))[20:24])

def get_lan_ip():
    ip = get_interface_ip("wlan1")
    return ip

def light_on():
   subprocess.call(["/sbin/insmod", "/root/sun4i-vibrator.ko"])
   print "turn on light now !!!"

def light_off():
   subprocess.call(["/sbin/rmmod", "sun4i_vibrator"])
   print "turn off light now !!!"

def send_reply(email_body):
   ps = subprocess.Popen(('echo', email_body), stdout=subprocess.PIPE)
   output = subprocess.check_output(( 'msmtp', '-a', 'default', 'peisheng.ye.88@gmail.com'), stdin=ps.stdout)
   ps.wait()

def getbody(message): #getting plain text 'email body'
    body = None
    if message.is_multipart():
        for part in message.walk():
            if part.is_multipart():
                for subpart in part.walk():
                    if subpart.get_content_type() == 'text/plain':
                        body = subpart.get_payload(decode=True)
            elif part.get_content_type() == 'text/plain':
                body = part.get_payload(decode=True)
    elif message.get_content_type() == 'text/plain':
        body = message.get_payload(decode=True)
    return body


def make_email(email_body):
   email_tile = 'Network status on A13 board'
   msg = MIMEText(email_body)
# me == the sender's email address
# you == the recipient's email address
   msg['Subject'] =  email_tile
   msg['From'] = 'nicolas.ye.88'
   msg['To'] = 'peisheng.ye.88@gmail.com'
   return msg.as_string() 

def get_current_time():
    current_time = datetime.datetime.now()
    local_time_ = current_time.isoformat()
    return local_time_    

def get_alive():
    remoteServerIPHEAD  = "192.168.12."
    result_str = ""

    try:
        local_ip =  get_lan_ip()
        print "local ip address" , local_ip
        result_str += "local ip is {}. ".format(local_ip)
        for ip in range(101,116):
            remoteServerIP_str = remoteServerIPHEAD + str(ip)
            if remoteServerIP_str != local_ip : 
                 remoteServerIP  = socket.gethostbyname(remoteServerIP_str)
                 print "-" * 60
                 print "Please wait, scanning remote host", remoteServerIP_str

                 for port in range(21,23):  
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    result = sock.connect_ex((remoteServerIP, port))
                    if result == 0:
                        print "Port {}: 	 Open".format(port)
                        result_str += " {} is alive. ".format(remoteServerIP_str)
                        result_str += get_current_time()
                        
                    sock.close()
                 print "-" * 60

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



subject_keyword = "light"
mbox = mailbox.mbox('/var/spool/mail/root')
to_remove = []
for key, msg in mbox.iteritems():
    subject = msg['subject']
    subject = subject.lower()
    compare = subject.find(subject_keyword)
    if compare != -1:
              print "subject about light is found"
              to_remove.append(key)
    else:
              print "subject about light NOT found"




light_on_keyword = "light on"
light_off_keyword = "light off"
length = len(to_remove)
if length > 0:
   print "The mailbox have total mail number: ", length 
   print " the last one is No ", to_remove[length - 1]
   last_item = to_remove[length - 1]
   message = mbox.get(last_item)
   mail_body = getbody(message)
   mail_body = mail_body.lower()
   compare = mail_body.find(light_on_keyword)
   if compare != -1: 
       light_on()
       network_status = get_alive()
       network_status += " < light on > "
       message_email = make_email(network_status)
       send_reply(message_email)

   compare = mail_body.find(light_off_keyword)
   if compare != -1: 
       light_off()
       network_status= get_alive()
       network_status += " < light off > "
       message_email = make_email(network_status)
       send_reply(message_email)
   mbox.lock()
   try:
       for key in to_remove:
          mbox.remove(key)
   finally: 
       mbox.flush()
       mbox.close()
   mbox.unlock()

else: 
   print "Nothing found" 




