import mysql.connector

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'your username',
    password = 'your password',
    database = 'hospital_management'
)

cursor = conn.cursor()
