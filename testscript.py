import psutil
import mysql.connector as connector
import csv

#TODO 
#listen on ftp 
#Assumes the database is already set up

#edit to match server
db = connector.connect(host="localhost",user="root",
                  passwd="server",db="ipro_db")
#change to match the new sql server parameters
add_proc = ("INSERT INTO processes "
               "(TIME, MACHINE_ID, PROCESS_NAME, MEMORY_UTILIZATION, CPU_UTILIZATION, MEMORY_USED, THREADS, USER, PATH, ID)"
               "VALUES (%s, %s, %s, %d, %d, %d, %d, %s, %s, %d )")
c = db.cursor()
#cursor.execute(sql, list(test.values()))
with open('foo.csv', newline='') as csvfile:
    print(csvfile)
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
    	#skip header row 
        if row[0] == "time":
            continue
        # row is a list, each position is a string based on the csv. 
        c.execute(add_proc, (row[0], row[1], row[2], int(row[3]), int(row[4]), int(row[5]), row[6], row[7], int(row[8]))
query = "SELECT * from processes"
c.execute(query)
