#!/usr/bin/env python3
# This example uses a credentials stored in a .env file defining SQL_HOST, SQL_USER, SQL_PWD, and SQL_DB

import mysql.connector, os
from dotenv import load_dotenv
load_dotenv()

def getConnection():
    connection = mysql.connector.connect(
        host=os.getenv('SQL_HOST'),
        user=os.getenv('SQL_USER'),
        password=os.getenv('SQL_PWD'),
        db=os.getenv('SQL_DB')
    )
    return connection

def printChampions():
    connection = getConnection()
    myCursor = connection.cursor()
    myCursor.execute("select * from champions")
    myResult = myCursor.fetchone()

    print("In the champions table, we have the following items: ")
    while myResult is not None:
        print(myResult)
        myResult = myCursor.fetchone()
    connection.close()
    print()

def printItem():
    connection = getConnection()
    myCursor = connection.cursor()
    myCursor.execute("select id, item_name from item")
    myResult = myCursor.fetchone()

    print("In the item table, we have the following items: ")
    while myResult is not None:
        print(myResult)
        myResult = myCursor.fetchone()
    connection.close()
    print()

def printItemsForChamps():
    connection = getConnection()
    myCursor = connection.cursor()
    champ_id = input("For which champion id would you like to view the items? ")
    myCursor.execute("select item.id, item_name from item join pref_item on item.id=pref_item.item_id where champion_id=%s", (champ_id,))
    myResult = myCursor.fetchall()
    print(f"There are {len(myResult)} items: ")
    for row in myResult:
        print(row)

def printChampsForItem():
    connection = getConnection()
    myCursor = connection.cursor()
    item_id = input("For which item id would you like to use to view champions? ")
    myCursor.execute("select champions.id, champions.name from champions join pref_item on champions.id=pref_item.champion_id and item_id=%s", (item_id,))
    myResult = myCursor.fetchall()
    print(f"There are {len(myResult)} champions: ")
    for row in myResult:
        print(row)

def addChampToItem():
    connection = getConnection()
    myCursor = connection.cursor()
    item_id = input("What item id are we going to add a champion to? ")
    champ_id = input("What champion id are we using? ")
    query = "insert into pref_item(item_id, champion_id) values(%s, %s);"
    myCursor.execute(query, (item_id, champ_id))
    connection.commit()
    connection.close()



def deleteChampFromItem():
    connection = getConnection()
    myCursor = connection.cursor()
    itemToDelete = input("Whats the item id we want? ")
    championToDelete = input("Whats the champion id we want? ")
    myCursor.execute("delete from pref_item where item_id=%s and champion_id=%s", (itemToDelete, championToDelete))
    connection.commit()
    connection.close()


menuText = """Please select one of the following options:
1) Print Champions
2) Print Items
3) Print Items for a Champion
4) Print Champions for an Item
5) Add an Champion to an Item (unimplemented)
6) Remove a Champion from an Item (unimplemented)
q) Quit
"""

if __name__ == "__main__":
    menuOption = "1"
    while menuOption != 'q':
        menuOption = input(menuText)
        if menuOption == "1":
            printChampions()
        elif menuOption == "2":
            printItem()
        elif menuOption == "3":
            printItemsForChamps()
        elif menuOption == "4":
            printChampsForItem()
        elif menuOption == "5":
            addChampToItem()
        elif menuOption == "6":
            deleteChampFromItem()