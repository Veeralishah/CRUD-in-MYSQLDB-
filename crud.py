#-*- coding: utf8 -*-

''' MYSQL CRUD '''

import MySQLdb as mdb
import sys
import warnings
from config import con


# CREATE A NEW TABLE
def createTable(con):
    with con:

        cur = con.cursor()
        cur.execute("DROP TABLE IF EXISTS Citizen")
        cur.execute("CREATE TABLE Citizen(Id INT PRIMARY KEY AUTO_INCREMENT, Firstname VARCHAR(25),Lastname VARCHAR(25), City VARCHAR(25), State VARCHAR(25), Country VARCHAR(25));")
        print 'Table created'

# INSERT VALUES
def insertTable(con):
    with con:

        try:
            cur = con.cursor()

            with warnings.catch_warnings():
                warnings.simplefilter('ignore')
                cur.execute("CREATE TABLE IF NOT EXISTS Citizen(Id INT PRIMARY KEY AUTO_INCREMENT, Firstname VARCHAR(25),Lastname VARCHAR(25), City VARCHAR(25), State VARCHAR(25), Country VARCHAR(25));")
                warnings.filterwarnings('ignore', 'unknown table')

            Id = 0
            Firstname = raw_input("Enter Your First Name ")
            Lastname = raw_input("Enter Your Last Name")
            City = raw_input("Enter Your City")
            State = raw_input("Enter Your State")
            Country = raw_input("Enter Your Country")
            cur.execute("INSERT INTO Citizen VALUES (%s, %s, %s, %s, %s, %s)",
                        (Id, Firstname, Lastname, City, State, Country))
            print "Record Inserted"
        except Exception as e:
            print e


# RETRIEVE TABLE ROWS
def retrieveTable(con):
    with con:

        cur = con.cursor(mdb.cursors.DictCursor)
        cur.execute("SELECT * FROM Citizen")

        rows = cur.fetchall()

        for row in rows:
            print row["Id"], row["Firstname"], row["Lastname"], row["City"], row["State"], row["Country"]


# UPDATE ROW
def updateRow(con):
    with con:

        try:
            cur = con.cursor()
            cur = con.cursor(mdb.cursors.DictCursor)
            cur.execute("SELECT * FROM Citizen")
            rows = cur.fetchall()
            for row in rows:
                print 'Table Data:', row["Id"], row["Firstname"], row["Lastname"], row["City"], row["State"], row["Country"]
            id = input("Enter ID for Update Record")
            city = raw_input('Enter City Name For Update record')
            cur.execute("UPDATE Citizen SET City = %s WHERE Id = %s",
                        ("city", "id"))
            print "Number of rows updated:",  cur.rowcount
            if cur.rowcount == 0:
                print 'Record Not Updated'
        except TypeError as e:
            print 'ID Not Exist '

 # DELETE ROW
def deleteRow(con):
    with con:

        try:
            cur = con.cursor()
            cur = con.cursor(mdb.cursors.DictCursor)
            cur.execute("SELECT * FROM Citizen")
            rows = cur.fetchall()
            for row in rows:
                print 'Table Data:', row["Id"], row["Firstname"], row["Lastname"], row["City"], row["State"], row["Country"]

            id = input("Enter ID for Delete Record")
            cur.execute("DELETE FROM Citizen WHERE Id = %s", id)
            print "Number of rows deleted:", cur.rowcount

        except TypeError as e:
            print 'ID Not Exist '
