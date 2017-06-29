#-*- coding: utf8 -*-

from config import con
from crud import *
import sys
import MySQLdb as mdb


'''Menu for User Input '''


def choice():
    print "1. Create Table"
    print "2. Insert Data"
    print "3. Read Data"
    print "4. Update Data"
    print "5. Delete Data"
    print "6. Quit"

    ch = input("Enter Your Choice")
    if ch == 1:
        createTable(con)
    elif ch == 2:
        insertTable(con)
    elif ch == 3:
        retrieveTable(con)
    elif ch == 4:
        updateRow(con)
    elif ch == 5:
        deleteRow(con)
    elif ch == 6:
        exit()
        pass
    else:
        print "Please Enter Valid Input"

choice()
