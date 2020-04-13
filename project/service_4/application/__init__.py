from flask import Flask, request
import requests
# from flask_mysqldb import MySQL

app = Flask(__name__)

# from application import routes

# app.config["MYSQL_HOST"] = '35.228.198.52'
# app.config["MYSQL_USER"] = 'root'
# app.config["MYSQL_PASSWORD"] = 'linternaverde'
# app.config["MYSQL_DB"] = 'SFIA2'

# mysql = MySQL(app)


@app.route('/game', methods=['GET'])
def game():
    computer1r = requests.get('http://34.89.103.64:5001/computer1')
    computer2r = requests.get('http://34.89.103.64:5002/computer2')
   
    if computer1r==computer2r:
        return("Computer1: " + computer1r + " vs computer2: " + computer2r +". Result: " + "Tie")
    if (computer1r=="Rock" and computer2r=="Paper") or (computer1r=="Paper"  and computer2r =="Scissors" ) or (computer1r=="Scissors"  and computer2r =="Rock" ):
        return ("Computer1: " + computer1r + " vs computer2: " + computer2r +". Result: Computer2 wins")

    if (computer2r=="Rock" and computer1r=="Paper") or (computer2r=="Paper"  and computer1r =="Scissors" ) or (computer2r=="Scissors"  and computer1r =="Rock" ):
        return ("Computer1: " + computer1r + " vs computer2: " + computer2r +". Result: Computer1 wins")
    