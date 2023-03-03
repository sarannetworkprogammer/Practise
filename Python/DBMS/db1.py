import mysql.connector

mydb =mysql.connector.connect(host = "localhost",user ="navin",passwd = "1234",database ="telsuko")

mycursor = mydb.cursor()

mycursor.execute("select * from student")



for i in mycursor:

    print(i)