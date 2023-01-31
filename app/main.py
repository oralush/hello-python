from flask import Flask
from flaskext.mysql import MySQL

app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = os.environ.get('MYSQL_USER', None)
app.config['MYSQL_DATABASE_PASSWORD'] = os.environ.get('MYSQL_PASS', None)
app.config['MYSQL_DATABASE_DB'] = os.environ.get('MYSQL_DB', None)
app.config['MYSQL_DATABASE_HOST'] = os.environ.get('MYSQL_HOST', None)
mysql = MySQL(app)
mysql.init_app(app)
conn = mysql.connect()




@app.route("/")
def hello():
    return "Hello from Python!"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
