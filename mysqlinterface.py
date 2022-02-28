import psutil
import mysql.connector as connector
import csv
import sys

#TODO 
#listen on ftp 
#Assumes the database is already set up

#edit to match server
db = connector.connect(host="ipro-db.crhoiczd7use.us-east-1.rds.amazonaws.com",user="admin",
                  passwd="$ecure_my5ql_p4ssw0rd1!",db="ipro_db")
#change to match the new sql server parameters
add_proc = ("INSERT INTO processes "
               "(TIME, MACHINE_ID, PROCESS_NAME, MEMORY_UTILIZATION, CPU_UTILIZATION, MEMORY_USED, THREADS, USER, PATH, ID)"
               "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s )")
c = db.cursor()
#csv file taken in argv[1} .
# Example usage: py testscript.py foo.csv
with open(sys.argv[1], newline='') as csvfile:
    print(csvfile)
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
    	#skip header row 
        if row[0] == "time":
            continue
        # row is a list, each position is a string based on the csv. 
        c.execute(add_proc, (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]))
query = "SELECT * from processes"
c.execute(query)
