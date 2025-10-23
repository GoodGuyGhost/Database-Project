#! /usr/bin/python3

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/getform')
def renderFormGet():
    output = render_template('form-get.html')
    return output 

@app.route('/gettable', methods=['GET'])
def renderTableGet():
    firstname = request.args.get('fname')
    lastname = request.args.get('lname')
    attacktype = request.args.get('ackTyp')
    output = render_template('table.html', firstname=firstname, lastname=lastname, attacktype=attacktype)
    return output 


if __name__ == '__main__':
    app.run(port=8000, debug=True, host="0.0.0.0")