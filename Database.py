import sqlite3
from django import db
from pipenv.vendor.vistir import rs
#from django import db

#connected to the sqlite3
db = sqlite3.connector('Registration')
    #created cursor from database registration
rs = db.cursor()

    
#created table name registration and number is varchar
rs.execute('''create table register(name varchar(50), email varchar(100), passwd varchar(10))''')
db.commit()

#Add data in table
rs.execute(''' insert into signup values('skkamal', '@gmail.com', 'sk123123') ''')
db.commit()


rs.execute('select * from signup')
for i in rs:
    print(i)