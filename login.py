#!/usr/bin/python3
import mysql.connector
from mysql.connector import errorcode
import cgi

data = cgi.FieldStorage()

data = cgi.FieldStorage()
nombre = data.getvalue('nombre')
password = data.getvalue('con')


try:
    cnx = mysql.connector.connect(
        user='Caceres', password='s28Nor04+', database='baseArquitectura', host='127.0.0.1')
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    cur = cnx.cursor()
    print('Content-Type: text/html')
    print('')
    sql = ("insert into CLIENTES values ('{}',SHA( '{}'))".format(nombre, password))
    cur.execute(sql)
    cnx.commit()
    print('<h1> Bienvenido {} </h1>'.format(nombre))

cnx.close()