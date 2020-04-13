from flask import Flask, request
import requests
#from flask_mysqldb import MySQL
import random

app = Flask(__name__)



# app.config["MYSQL_HOST"] = '35.228.198.52'
# app.config["MYSQL_USER"] = 'root'
# app.config["MYSQL_PASSWORD"] = 'linternaverde'
# app.config["MYSQL_DB"] = 'SFIA2'

# mysql = MySQL(app)





@app.route('/computer2', methods=['GET'])

def computer2():
    computer2=["Rock", "Paper", "Scissors"]
	
    return computer2[random.randrange(2)]
    
