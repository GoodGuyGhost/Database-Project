#! /usr/bin/python3

from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json

app = Flask(__name__) # creates a flask application object

with open('secrets.json', 'r') as secretFile:
    creds = json.load(secretFile)['mysqlCredentials']

# example database uri = "mysql+pymysql://jeff:mypass@localhost/sakila"
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{creds['user']}:{creds['password']}@{creds['host']}/{creds['db']}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Staff(db.Model):
    staff_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    email = db.Column(db.String)
    username = db.Column(db.String)
    password = db.Column(db.String)
    last_update = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now())

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/create')
def create():
    return render_template("createform.html")

@app.route('/newStaff')
def insert():
    staff = Staff(first_name=request.args.get("firstName"), last_name=request.args.get("lastName"), email=request.args.get("email"), username=request.args.get("username"), password=request.args.get("password"))
    db.session.add(staff)
    db.session.commit()
    return redirect("read")

@app.route('/updateform')
def updateform():
    staff = Staff.query.get(request.args.get("id"))
    return render_template("updateform.html", staff=staff)

@app.route('/update')
def update():
    staff = Staff.query.get(request.args.get("id"))
    staff.first_name = request.args.get("firstName")
    staff.last_name = request.args.get("lastName")
    staff.email = request.args.get("email")
    staff.username = request.args.get("username")
    staff.password = request.args.get("password")
    db.session.commit()
    return redirect("read")

@app.route('/delete')
def remove():
    staff = Staff.query.get(request.args.get("id"))
    db.session.delete(staff)
    db.session.commit()
    return redirect("read")


@app.route('/read')
def read():
    staff = Staff.query.all()
    output = render_template("showactors.html", staff=staff)
    return output

if __name__ == '__main__':
    app.run(port=8000, debug=True, host="0.0.0.0")