import pymysql

import os
from dotenv import load_dotenv

load_dotenv()

# Replace these values with your MySQL database details
HOST = os.environ.get("HOST")
USER = os.environ.get("USERNAME")
PASSWORD = os.environ.get("PASSWORD")
DATABASE = os.environ.get("DATABASE")

# Test the connection to MySQL
try:
    connection = pymysql.connect(host=HOST, user=USER, password=PASSWORD, database=DATABASE)
    print("Connection to MySQL database successful.")

    # Optionally, perform a simple query
    with connection.cursor() as cursor:
        cursor.execute("SELECT VERSION();")
        version = cursor.fetchone()
        print("Database version:", version)

    # Close the connection
    connection.close()
except pymysql.MySQLError as e:
    print("Error connecting to MySQL database:", e)
