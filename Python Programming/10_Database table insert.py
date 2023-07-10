import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="ece"
)

mysql=mydb.cursor()
sql="insert into students (name, address, email) values(%s,%s,%s)"
a=str(input("Enter name: "))
b=str(input("Enter address: "))
c=str(input("Enter email: "))
      
val=(a,b,c)
mysql.execute(sql,val)

mydb.commit()

print(mysql.rowcount, "record inserted")