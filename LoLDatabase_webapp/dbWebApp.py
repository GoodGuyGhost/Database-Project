#!/usr/bin/python3

from flask import Flask, render_template, request
import mysql.connector, os
import json


app = Flask(__name__)


@app.route('/', methods=['GET'])
def showSpeakers():
    with open('/home/dylan/Database-Project/LoLDatabase_webapp/secrets.json', 'r') as secretFile:
        creds = json.load(secretFile)['mysqlCredentials']

    connection = mysql.connector.connect(**creds)

    mycursor = connection.cursor()

    # If there is a name and desc 'GET' variable, insert the new value into the database
    newname = request.args.get('champname')
    neworigin = request.args.get('champorigin')
    newatk = request.args.get('champatk')
    if newname is not None and neworigin is not None and newatk is not None:
        mycursor.execute("INSERT into champions (name, origin, attack_style) values (%s, %s, %s)", (newname, neworigin, newatk))
        connection.commit()

    # Fetch the current values of the speaker table
    mycursor.execute("Select name, origin, attack_style from champions")
    myresult = mycursor.fetchall()
    mycursor.close()
    connection.close()
    return render_template('champ-list.html', collection=myresult)
    #return "Hello world"


if __name__ == '__main__':
    app.run(port=8000, debug=True, host="0.0.0.0")