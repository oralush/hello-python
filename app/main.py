from flask import Flask
import mysql.connector
from mysql.connector import Error



app = Flask(__name__)


try:
    connection = mysql.connector.connect(host='localhost',
                                         database='or_db',
                                         user='python',
                                         password='python')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
        
@app.route("/")
def main():
    def hello():
        return "Hello from Python!"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
