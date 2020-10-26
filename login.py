#!/usr/bin/python3
import mysql.connector
from mysql.connector import errorcode
import cgi

data = cgi.FieldStorage()

correo = data.getvalue('correo')
password = data.getvalue('pass')


try:
    cnx = mysql.connector.connect(user='Caceres', password='s28Nor04+', database='baseArquitectura', host='127.0.0.1')
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
    sql = ("select* from Usuario where Email = '{}' and contraseña = SHA('{}')  ".format(correo, password))
    cur.execute(sql)
    com = cur.fetchall()
    if com:
        print('<script> location.href="/Entregable2CorteSoftware/index.html";</script>')
    else:
        print('<h1> Fallo </h1>')
        cnx.commit()

cnx.close()