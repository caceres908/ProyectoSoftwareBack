import mysql.connector
from mysql.connector import errorcode
from flask import Flask 
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
	return "Hello friend";

@app.route('/productosM', methods=['GET'])
def mostrar_productos():
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

@app.route('/productosMO', methods=['PUT'])
def modificar_productos():
	return "Modificando producto uwu";

@app.route('/productosB', methods=['DELETE'])
def borrar_productos():
	return "borrando producto unu";

@app.route('/productosC', methods=['POST'])
def crear_productos():
	return "creando producto ewe";

if __name__ == "__main__":
	app.run(host = '0.0.0.0')    

