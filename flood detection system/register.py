from flask import Flask,render_template,url_for,request,redirect, make_response
from multiprocessing import connection
from flask import Flask, render_template, make_response
import sqlite3 
import os

currentdirectory = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def main():
    return render_template('index2.html')

@app.route('/signup', methods=["GET", "POST"])
def signup():
    if request.method == "POST":
     aname = request.form["aname"]
     bname = request.form["bname"]
     cname = request.form["cname"]
     dname = request.form["dname"]
     ename = request.form["ename"]
    
     connection = sqlite3.connect(currentdirectory + "\database.db")
     cursor = connection.cursor()
     query1 = "INSERT INTO RecipientDetails VALUES('{an}','{b}','{cb}',{dc},'{e}')".format( an = aname, b = bname, cb = cname, dc = dname, e=ename)
     cursor.execute(query1)
     connection.commit()
     return redirect("/confirmation")
    return render_template('signup.html')

@app.route('/confirmation', methods=["GET", "POST"])
def confirmation():
    return render_template('confirmation.html')
if __name__ == "__main__":
    app.run(debug=True)