from flask import Flask 

app = Flask(__name__)

@app.route('/')
def hellos():
	return "Hello friend";

@app.route('/productosM', methods=['GET'])
def mostrar_productos():
	return "Mostrando productos owo";

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

