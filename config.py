#-*- coding: utf8 -*-

import MySQLdb as mdb
import warnings

# CREATE THE DATABASE


def createdb_mysql():
    db = mdb.connect(host="localhost", user="root", passwd="PASSWORD")
    db1 = db.cursor()
    with warnings.catch_warnings():
        warnings.simplefilter('ignore')
        db1.execute('CREATE DATABASE IF NOT EXISTS testdb')
        print('Create Database testdb')


# SET UP THE CONNECTION


try:
    con = mdb.connect('localhost', 'root', 'PASSWORD', 'testdb')
    cur = con.cursor()
    cur.execute("SELECT VERSION()")
    ver = cur.fetchone()
    print "Database version : %s " % ver


except mdb.Error, e:

    print "Error %d: %s" % (e.args[0], e.args[1])
    sys.exit(1)


createdb_mysql()
