import pytest
import urllib3
from flask import Flask, render_template, request
import os
#rom flask_mysqldb import MySQL
import requests
#import csv

#app = Flask(__name__)

#app.config['MYSQL_HOST']=os.environ['MYSQL_HOST']
#app.config['MYSQL_USER']=os.environ['MYSQL_USER']
#app.config['MYSQL_PASSWORD']=os.environ['MYSQL_PASSWORD']
#app.config['MYSQL_DB']=os.environ['MYSQL_DB']

#mysql = MySQL(app)

url = "http://35.242.162.195/"
url2 = "http://35.188.1.233/"

def test_node_manager():
    http = urllib3.PoolManager()
    r = http.request('GET', url)
    assert 200 == r.status

def test_node_worker():
    http = urllib3.PoolManager()
    r = http.request('GET', url2)
    assert 200 == r.status

def test_getresponse():
    r = requests.get(url2)
    assert isinstance(r.text, str)

def test_getresponse2():
    r = requests.get(url)
    assert isinstance(r.text, str)

