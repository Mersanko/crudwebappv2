from flask import Flask
from flask_mysqldb import MySQL
import yaml


app = Flask(__name__)


db = yaml.load(open('config.yaml'))
app.secret_key = db['secret_key']
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']


mysql = MySQL(app)
from app import routes