import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="ece"
)

mysql_query=mydb.cursor()

mysql_query.execute("create table students (id int auto_increment primary key, name varchar(255), address varchar(255), email varchar(255))")