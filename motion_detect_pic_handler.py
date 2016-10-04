#!/usr/bin/python
import glob, os

def send_reply(email_body):
   ps = subprocess.Popen(('echo', email_body), stdout=subprocess.PIPE)
   output = subprocess.check_output(( 'msmtp', '-a', 'default', 'peisheng.ye.88@gmail.com'), stdin=ps.stdout)
   ps.wait()

cmd_mutt = ["mutt",  "-s", "Motion detected ", "peisheng.ye.88@gmail.com", "-a"] 


os.chdir("/root/motion2_events/")
fileListSorted = []
fileMap = {}
filelist = glob.glob("*.jpg")
length = len(filelist)
#print(length)
for name in filelist :
    token = name.split('-', 1) 
#    print(token[1])
    fileListSorted.append(token[1])
    fileMap[token[1]]=name
    

fileSortedList = sorted(fileListSorted)
length = len(fileSortedList)
lastOne = fileSortedList[length -1]
lastOneFilename = fileMap[lastOne]
#print(length)
#print(lastOne)
#print(lastOneFilename)
lastTenFileName = []
length = length -10
if length > 0:
    lastTenFile = fileSortedList[length:]
else:
    lastTenFile = fileSortedList


for each in lastTenFile:
#    print(each)
    fileName = fileMap[each]
    lastTenFileName.append(fileName)   

for each in lastTenFileName:
    print(each)

 



