from flask import Flask, request, render_template
import requests



app = Flask(__name__)

#from application import routes

@app.route('/', methods=['GET'])
@app.route('/index')
def home():
    result = requests.get('http://35.242.162.195:5003/game')                              #####change local host to your own external ip in gcp vm
    #print(result)
    sentence = result.text
    return render_template('index.html', sentence = sentence, title = 'Home')