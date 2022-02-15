import psutil
import mysql.connector as connector
import csv

#Assumes the database is already set up
#edit to match server
db = connector.connect(host="localhost",user="root",
                  passwd="server",db="ipro_db")
#change to match the new sql server parameters
add_proc = ("INSERT INTO processes "
               "(PROCESS_ID, PROCESS_NAME, MEM_USAGE, CPU_USAGE)"
               "VALUES (%i, %s, %i, %i)")
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
        c.execute(add_proc, (1, row[2], row[3], row[4]))
query = "SELECT * from processes"
c.execute(query)
