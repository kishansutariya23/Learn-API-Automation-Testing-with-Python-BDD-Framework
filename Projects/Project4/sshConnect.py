import paramiko as paramiko
from utilities.configuration import *

# as wrote in database follow same method so that code will be clean
# start connection
username = getConfig()['server']['username']
password = getConfig()['server']['password']
host = getConfig()['server']['host']
port = getConfig()['server']['port']

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host,port,username,password)


# run commands
# for stdin sometime we have to give password manually multiple time so with this we can reducing the step
# command o/p is store in stdout
#  if any error then the log will be store in stderr
stdin, stdout, stderr = ssh.exec_command('ls -a')
print(stdout.readlines()) # send list
# if once the file is read and one more time you are running the same command then you will get error of out-of-index
# same as of readlines of csv and in SQL
# so make sure you comment out the readlines and run to see proper o/p

# if we give command to see the file content with cat
lines = stdout.readlines()
print(lines[0])
# by below loop we can see the exact file type
for line in lines:
    print(line)

ssh.close()





