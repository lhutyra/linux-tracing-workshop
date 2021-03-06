#!/usr/bin/env python

import sys
import mysql.connector

def insert():
    cursor = connection.cursor()
    try:
        cursor.execute("drop table employees")
    except:
        pass
    cursor.execute("create table employees (id integer primary key, name text)")
    cursor.close()

    print("Inserting employees...")
    for n in xrange(0, 10000):
        cursor = connection.cursor()
        cursor.execute("insert into employees (id, name) values (%d, 'Employee_%d')" %
                       (n, n))
        connection.commit()
        cursor.close()

def select():
    print("Selecting employees...")
    while True:
        cursor = connection.cursor()
        cursor.execute("select * from employees where name like '%1417773'")
        for row in cursor:
            pass
        cursor.close()

connection = mysql.connector.connect(host='localhost', database='test')

if "insert" in sys.argv:
    while True:
        insert()
elif "insert_once" in sys.argv:
    insert()
elif "select" in sys.argv:
    select()
else:
    print("USAGE: data_access.py <insert|insert_once|select>")

connection.close()
