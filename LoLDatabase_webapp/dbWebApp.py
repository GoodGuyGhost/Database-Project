#!/usr/bin/python3

from flask import Flask, render_template, request, redirect, url_for
import mysql.connector, os, json

with open('/home/dylan/Database-Project/LoLDatabase_webapp/secrets.json', 'r') as secretFile:
        creds = json.load(secretFile)['mysqlCredentials']

connection = mysql.connector.connect(**creds)
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
     return render_template('base.html')

@app.route('/showChamp', methods=['GET'])
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

@app.route("/showItem", methods=['GET'])
def showItem():
    connection = mysql.connector.connect(**creds)
    mycursor = connection.cursor()
    mycursor2= connection.cursor()

    
    champID = request.args.get('champion_id')
    if champID is not None:
        
        itemId = request.args.get('item_id')
        if itemId is not None:
            mycursor.execute("""INSERT into pref_item (champion_id, item_id) values (%s, %s)
                             """, (champID, itemId))
            connection.commit()

        mycursor.execute("""select item.id, item_name, attack_damage, ability_power, armor, champions.name
                         from item 
                         join pref_item on item.id=pref_item.item_id 
                         join champions on champions.id=pref_item.champion_id
                         where champion_id=%s""", (champID,))
        items = mycursor.fetchall()
        print(items)
        
        
        
        if len(items) >= 1:
            champName = items[0][5]
            mycursor.execute("""select distinct item.id, item_name from item join pref_item on item.id=pref_item.item_id where item.id not in(select item_id from pref_item where pref_item.champion_id=%s)""", (champID,))
            otheritems = mycursor.fetchall()
            print(otheritems)
        elif champID is not None:
            mycursor2.execute("select champions.name from champions where champions.id=%s",(champID,))
            champName = mycursor2.fetchall()
            mycursor.execute("""select distinct item.id, item_name from item join pref_item on item.id=pref_item.item_id where item.id not in(select item_id from pref_item where pref_item.champion_id=%s)""", (champID,))
            otheritems = mycursor.fetchall()
            print(otheritems)
        else:
            champName = "Unknown"
            otheritems = None
        
        pageTitle = f"Showing all items: {champName}"
    else:
        mycursor.execute("SELECT id, item_name, attack_damage, ability_power, armor from item")
        pageTitle = "Showing all items"
        items = mycursor.fetchall()
        otheritems = None

    mycursor.close()
    connection.close()
    print(f"{champID=}")
    return render_template('items.html', itemList=items, pageTitle=pageTitle, otheritems=otheritems, champId=champID )

@app.route("/showPrefItem", methods=['GET'])
def showPrefItem():
    connection = mysql.connector.connect(**creds)
    mycursor = connection.cursor()

    itemId = request.args.get('item_id')
    if itemId is not None:
        mycursor.execute("""SELECT champions.id, champions.name, origin, attack_style, item_name from champions 
                         join pref_item on champions.id=pref_item.champion_id
                         join item on item.id=pref_item.item_id
                         where item.id=%s""", (itemId,))
        myresult = mycursor.fetchall()
        print(myresult)
        if len(myresult) >= 1:
            itemName = myresult[0][4]
        else:
            itemName = "Unknown"
        pageTitle = f"Showing all champions that use the item {itemName}, item ID is: {itemId} )"
    else:
        mycursor.execute("SELECT id, name, origin, attack_style from champions")
        pageTitle = "Showing all Champions"
        myresult = mycursor.fetchall()

    mycursor.close()
    connection.close()
    return render_template('item-pref.html', championList=myresult, pageTitle=pageTitle)

'''
@app.route("/addItem", methods=['GET'])
def addItem():
    mycursor = connection.cursor()

    # If there is a name and desc 'GET' variable, insert the new value into the database
    newname = request.args.get('itemname')
    newdps = request.args.get('dps')
    newap = request.args.get('ap')
    newarmor = request.args.get('armor')
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
'''
if __name__ == '__main__':
    app.run(port=8000, debug=True, host="0.0.0.0")