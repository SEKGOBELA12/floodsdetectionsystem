from flask import Flask,render_template,url_for,request,redirect, make_response
import random
import json
from distutils.log import debug
from multiprocessing import connection
from time import time
from random import random
from flask import Flask, render_template, make_response
import sqlite3 
import os

currentdirectory = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def main():
    return render_template('index.html')

@app.route('/LoginRError', methods=["GET", "POST"])
def LoginRError():
    return render_template('LoginRError.html')

@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method =="POST":
        email = request.form["email"]
        password = request.form["password"]
        connection = sqlite3.connect(currentdirectory + "\database.db")
        cursor = connection.cursor()
        query1 = "SELECT username, password FROM admin_Details WHERE username = '{un}' AND password = '{pw}'".format(un = email, pw = password)
     
        cursor.execute(query1)
        rows = cursor.fetchall()
        if len(rows) == 0:
          return redirect(url_for('LoginRError'))
        else:
         return render_template("dashboard.html")
      
     
    return render_template('login.html')

@app.route('/dashboard', methods=["GET", "POST"])
def dashboard():
    if request.method == "POST":
     fname = request.form["temperature"]
     gname = request.form["humidity"]
     hname = request.form["waterLevel"]
    
    
     connection = sqlite3.connect(currentdirectory + "\database.db")
     cursor = connection.cursor()
     query1 = "INSERT INTO floodsValues VALUES({an},{b},{cb})".format( an = fname, b = gname, cb = hname)
     cursor.execute(query1)
     connection.commit()
     

    return render_template('dashboard.html')


@app.route('/data', methods=["GET", "POST"])
def data():
    # Data Format
    # [TIME, Temperature, Humidity, WaterLevel]

    Temperature = random() * 15
    Humidity = random() * 10
    WaterLevel = random() * 2

    data = [time() * 1000, Temperature, Humidity, WaterLevel]

    response = make_response(json.dumps(data))

    response.content_type = 'application/json'

    return response


if __name__ == "__main__":
    app.run(debug=True)