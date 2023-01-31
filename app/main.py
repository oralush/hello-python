from flask import Flask
from flaskext.mysql import MySQL
import os

app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = os.environ.get('MYSQL_USER', None)
app.config['MYSQL_DATABASE_PASSWORD'] = os.environ.get('MYSQL_PASS', None)
app.config['MYSQL_DATABASE_DB'] = os.environ.get('MYSQL_DB', None)
app.config['MYSQL_DATABASE_HOST'] = os.environ.get('MYSQL_HOST', None)
mysql = MySQL(app)
mysql.init_app(app)
conn = mysql.connect()

@app.route("/")
def main():
    cursor = conn.cursor()
    cursor.execute('''SELECT text FROM data WHERE id = 1''')
    rv = cursor.fetchall()
    return rv[0]

if __name__ == "__main__":
    app.run(host='0.0.0.0')
