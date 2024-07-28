import mysql.connector
import os

def create_database(cursor):
    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")
    except mysql.connector.Error as err:
        print(f"Failed creating database: {err}")

def main():
    try:
        user = os.getenv('MYSQL_USER')
        password = os.getenv('MYSQL_PASSWORD')

        if user is None or password is None:
            raise ValueError("MySQL username or password not set in environment variables")

        
        cnx = mysql.connector.connect(
            user=user,
            password=password
        )
        cursor = cnx.cursor()
        create_database(cursor)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        else:
            print(err)
    except ValueError as verr:
        print(verr)
    else:
        cursor.close()
        cnx.close()

