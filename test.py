from datetime import datetime 
import mysql.connector as m 
db=m.connect(host='localhost',
        user='root',
        passwd='45924572',
        database='bank_of_kv')
cur=db.cursor()
print(datetime.datetime('2020, 12, 25').strftime('%Y-%m-%d'))
        