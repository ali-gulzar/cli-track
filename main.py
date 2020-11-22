import psycopg2
import sys

connection = psycopg2.connect("dbname=device_report user=AliGulzar password=tramigo host=localhost")
cursor = connection.cursor()
cursor.execute(open("../device_report.sql", "r").read())

if (sys.argv[1] == 'track'):
    cursor.execute('SELECT * FROM reports JOIN devices ON devices.id = reports.device_id')
    rows = cursor.fetchall()
    print(rows)

cursor.close()
connection.close()