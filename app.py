#!/usr/bin/python3
import mysql.connector
from mysql.connector import errorcode
import flask
from flask import Flask, jsonify, request
from flask_cors import CORS
import json

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)

app.config.from_object(__name__)

# enable CORS


CORS(app)
@app.route('/')
def hellos():
    return "Hello friend"

try:
    app = flask.Flask(__name__)
    app.config["DEBUG"] = True
    cnx = mysql.connector.connect(user='Caceres', password='s28Nor04+', database='baseProyecto', host='127.0.0.1')
    CORS(app)
    @app.route('/usuarioC', methods=['POST']) 
    def puntua2():
        cur = cnx.cursor()
        data = request.get_json(force=True)
        nom = data.get('nombre')
        ema = data.get('correo')
        con = data.get('con')
        tel = data.get('tel')
        dire = data.get('dire')
        cur.execute("insert into Usuario (nombre,Email,contraseña,numero,direccion) values (%s,%s,%s,%s,%s)", (nom,ema,con,tel,dire))
        cnx.commit()
        cur.close()
        return ("1")
    CORS(app)
    @app.route('/usuarioG', methods=['GET'])
    def datos_get():
        cur = cnx.cursor()
        sql = ("select * from Usuario ")
        cur.execute(sql)
        row = cur.fetchall()
        lista = list()
        for i in row:
            iden = i[0] 
            nom = i[1]
            email = i[2]
            contra = i[3]
            tel = i[4]
            dire = i[5]
            persona = {'Id': iden,
                       'Nombre': nom,
                       'Email': email,
                       'password': contra,
                       'Telefono': tel,
                       'Direccion': dire, }
            lista.append(persona)
            cnx.commit()
            cur.close()
        return jsonify(results=lista)
    CORS(app)
    @app.route('/usuariop', methods=['PUT'])
    def actualizar():
        cur = cnx.cursor(buffered=True)
        data = request.get_json(force=True)
        nom = data.get('nombre')
        ema = data.get('correo')
        con = data.get('con')
        tel = data.get('tel')
        dire = data.get('dire')
        cur.execute("update Usuario Set nombre = %s,contraseña = %s,numero= %s,direccion= %s  where Email = %s",(nom,con,tel,dire,ema))
        cnx.commit()
        cur.close()
        return("2")
    CORS(app)
    @app.route('/usuariob', methods=['DELETE'])
    def borrar_usuario():
        cur = cnx.cursor(buffered=True)
        data = request.get_json(force=True)
        ema = data.get('correo')
        cur.execute("delete from Usuario where Email = '{}'".format(ema))
        cnx.commit()
        cur.close()
        return("3")
    CORS(app)
    @app.route('/productosG', methods=['GET'])
    def preductos_get():
        cur = cnx.cursor()
        sql = ("select * from Productos ")
        cur.execute(sql)
        row = cur.fetchall()
        lista = list()
        for i in row:
            cod = i[0] 
            nom = i[1]
            des = i[2]
            pre = i[3]
            img = i[4]
            cat = i[5]
            persona = {'Codigo': cod,
                       'Nombre': nom,
                       'Descripcion': des,
                       'Precio': pre,
                       'Imagen': img,
                       'Categoria': cat}
            lista.append(persona)
            cnx.commit()
            cur.close()
        return jsonify(results=lista)
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
app.run(host='0.0.0.0',debug=True)
        

