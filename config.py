#-*- coding: utf8 -*-

import MySQLdb as mdb

# CREATE THE DATABASE

db = mdb.connect(host="localhost", user="USERNAME", passwd="PASSWORD")
db1 = db.cursor()
db1.execute('CREATE DATABASE dbname')


# SET UP THE CONNECTION

try:
    con = mdb.connect('localhost', 'USERNAME', 'PASSWORD', 'DATABASE')
    cur = con.cursor()

except mdb.Error, e:

    print "Error %d: %s" % (e.args[0], e.args[1])
    sys.exit(1)
