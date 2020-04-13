from flask import Flask, request
import requests
#from application import app
# from flask_mysqldb import MySQL
# #from application import routes
# #import pandas as pd 
# import MySQLdb
import random


app = Flask(__name__)



# app.config["MYSQL_HOST"] = '35.228.198.52'
# app.config["MYSQL_USER"] = 'root'
# app.config["MYSQL_PASSWORD"] = 'linternaverde'
# app.config["MYSQL_DB"] = 'SFIA2'

# mysql = MySQL(app)



@app.route('/computer1', methods=['GET'])
def computer1():
	computer1=["Rock", "Paper", "Scissors"]
	
	return computer1[random.randrange(2)]