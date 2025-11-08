#!/usr/bin/python3

from flask import Flask, render_template, request, redirect, url_for
import mysql.connector, os, json

with open('/home/dylan/Database-Project/LoLDatabase_webapp/secrets.json', 'r') as secretFile:
        creds = json.load(secretFile)['mysqlCredentials']

connection = mysql.connector.connect(**creds)
app = Flask(__name__)


@app.route('/', methods=['GET'])
def showChamp():
    mycursor = connection.cursor()

    # If there is a name and desc 'GET' variable, insert the new value into the database
    newname = request.args.get('champname')
    neworigin = request.args.get('champorigin')
    newatk = request.args.get('champatk')
    if newname is not None and neworigin is not None and newatk is not None:
        mycursor.execute("INSERT into champions (name, origin, attack_style) values (%s, %s, %s)", (newname, neworigin, newatk))
        connection.commit()
    elif request.args.get('delete') == 'true':
        deleteID = request.args.get('id')
        mycursor.execute("DELETE from champions where id=%s", (deleteID,))
        connection.commit()

    # Fetch the current values of the speaker table
    mycursor.execute("Select id, name, origin, attack_style from champions")
    myresult = mycursor.fetchall()
    mycursor.close()
    return render_template('champ-list.html', collection=myresult)

@app.route("/updateChampion")
def updateChamp():
    id = request.args.get('id')
    name = request.args.get('champname')
    origin = request.args.get('champorigin')
    attackstyle = request.args.get('champatk')
    if id is None:
        return "Error, id not specified"
    elif name is not None and origin is not None and attackstyle is not None:
        mycursor = connection.cursor()
        mycursor.execute("UPDATE champions set name=%s, origin=%s, attack_style=%s where id=%s", (name, origin, attackstyle, id))
        mycursor.close()
        connection.commit()
        return redirect(url_for('showChamp'))

    mycursor = connection.cursor()
    mycursor.execute("Select name, origin, attack_style from champions where id=%s;", (id,))
    existingName, existingOrigin, existingAtk = mycursor.fetchone()
    mycursor.close()
    return render_template('champ-update.html', id=id, existingName=existingName, existingOrigin=existingOrigin, existingAtk=existingAtk)



if __name__ == '__main__':
    app.run(port=8000, debug=True, host="0.0.0.0")