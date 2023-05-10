import mysql.connector
# host,DB,USER,PASSWORD
conn = mysql.connector.connect(host='localhost',database=' APIDevelop',
                        user='root',password='')
print(conn.is_connected())
cursor = conn.cursor()
# print(cursor)
# cursor if in 2nd line and its fetch again then from 2nd line to nth line it will print and 1st line it will miss
# it is similar to csv format-->read,write
# cursor.execute('select * from Books;')
# row = cursor.fetchone()
# print(row)
# print(row[3])
# sql result are in tuples




# below gives list of tuple
# cursor.execute('''select * from CustomerInfo;''')
# rowAll = cursor.fetchall()
# print(rowAll)



cursor.execute('''select * from CustomerInfo;''')
rows = cursor.fetchall()
sum=0
for row in rows:
    print(row[2])
    sum+=row[2]

print('Total sum of Customer ',sum)



# query = "UPDATE customerInfo set location='us' where CourseName='Jmeter'"
query = "UPDATE customerInfo set location=%s where CourseName=%s"
data = ('uk','Jmeter')
cursor.execute(query,data)
conn.commit()

cursor.execute('''select * from CustomerInfo;''')
rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()