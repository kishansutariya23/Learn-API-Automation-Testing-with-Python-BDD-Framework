# upload and download
import csv

import paramiko as paramiko
from utilities.configuration import *

# start connection
username = getConfig()['server']['username']
password = getConfig()['server']['password']
host = getConfig()['server']['host']
port = getConfig()['server']['port']

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host,port,username,password)

# use SFTP protocol to upload and download the file
# upload files
sftp = ssh.open_sftp()
destinationPath = 'script.py'
localPath = 'Project4/batchfiles/script.py'
sftp.put(localPath,destinationPath)

# you can write code in utlility so that no need for multi writing the same code
destinationPath = 'loanasa.csv'
localPath = 'Project4/batchfiles/loanasa.csv'
sftp.put(localPath,destinationPath)



# trigger the batch command
stdin, stdout, stderr = ssh.exec_command('python script.py')



# download the file
sftp.get('loanasa.csv','batchfiles/output/loanasa.csv')

# you can open the csv files in read mode and print the o/p in terminal
with open('batchfiles/output/loanasa.csv') as csvFile:
    csvReader = csv.reader(csvFile,delimeter=',')
    for row in csvReader:
        if row[0]=='32321':
            assert row[1] == 'rejected'
#             we are checking the o/p in csv with our guts(as we know for this there should be rejection
# if we get assertion error then there is bug in script or batch script


ssh.close()