import os 
import shutil
import subprocess
# tutorial to schedule task once ftp up: https://www.geeksforgeeks.org/scheduling-python-scripts-on-linux/
#script should be scheduled to run from ftp server
#path should be the upload folder of the ftp
src_path = '/FTPROOT/upload'
dest_path = '/FTPROOT/archive'
for x in os.listdir(path):
	if x.endswith(".csv"):
		subprocess.call(['py' , 'mysqlinterface.py' , x])
		shutil.move((src_path+x), (dest_path+x))
