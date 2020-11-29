#!/usr/bin/python3
import mysql.connector
from mysql.connector import errorcode
from flask import Flask, jsonify, request
from flask_cors import CORS
import json

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)

app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/')
def hellos():
    return "Hello friend"


@app.route('/usuarioG', methods=['GET'])
def mostrar_usuarios():
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
        lista = list()
        for i in row:
            nom = i[0]
            email = i[1]
            contra = i[2]
            tel = i[3]
            dire = i[4]
            persona = {'Nombre': nom,
                       'Email': email,
                       'password': contra,
                       'Telefono': tel,
                       'Direccion': dire, }
            lista.append(persona)
        return jsonify(results=lista)
    cnx.close()


@app.route('/productosMO', methods=['PUT'])
def modificar_productos():
    return "Modificando producto uwu"


@app.route('/productosB', methods=['DELETE'])
def borrar_productos():
    return "borrando producto unu"


@app.route('/usuarioC', methods=['GET','POST'])
def crear_usuario():
    post_data = request.get_json()
    nom = post_data.get('nombre')
    ema = post_data.get('correo')
    con = post_data.get('con')
    tel = post_data.get('tel')
    dire = post_data.get('dire')
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
        sql = ("insert into Usuario (nombre,Email,contraseña,numero,direccion) values ('{}','{}',SHA( '{}'),'{}','{}')".format(nom,ema,con,tel,dire))
        cur.execute(sql)
        cnx.commit()
    cnx.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0')
