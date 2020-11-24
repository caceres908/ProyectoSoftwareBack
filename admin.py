#!/usr/bin/python3

from jinja2 import Template
import mysql.connector
from mysql.connector import errorcode
import cgi
import json


def infoBD(nombre, email, contraseña, telefono, direccion):
    with open('/var/www/html/Entregable2CorteSoftware/admin.html') as f:
        doc = f.read()
        template = Template(doc)
        page = template.render(nom=nombre, correo=email,
                               passw=contraseña, phone=telefono, add=direccion)
        print(page)


data = cgi.FieldStorage()

print('Content-Type: text/json')
print('')


try:
    cnx = mysql.connector.connect(
        user='Caceres', password='s28Nor04+', database='baseProyecto', host='127.0.0.1')
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    cur = cnx.cursor()
    
    sql = ("select* from Usuario ")
    cur.execute(sql)
    row = cur.fetchall()
    print('[')
    lon = len(row)
    j = 1
    for i in row:
        nom = i[0]
        email = i[1]
        contra = i[2]
        tel = i[3]
        dire = i[4]
        datos = {
            'Nombre': nom,
            'Email': email,
            'password': contra,
            'Telefono': tel,
            'Direccion': dire,
        }
        datos_json = json.dumps(datos)
        print(datos_json)
        if j < lon:
          print(',')
          j=j+1
        '''infoBD(nom,email,contra,tel,dire)'''
    print(']')

cnx.close()
