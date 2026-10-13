#pip install mysql
#pip install mysql-connector





import mysql.connector

dataBase = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="django_user",
    password="a_strong_password",
    database="mydb"
)



cursorObject = dataBase.cursor()

print("All done!")