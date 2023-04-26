from flask import Flask, jsonify
from find_uf import SII
import traceback 
app = Flask(__name__)

@app.route('/api/uf/<string:date>', methods=['GET'])
def getUFCurrency(date:str):
    try:
        value = SII.find_uf(date)
        if type(value) == bool:
            if value:
                msg = jsonify("La fecha ingresada no contiene registro, apartir del 01-01-2013 hay registros del UF")
            else:
                msg = jsonify("El formato ingresado no es correcto (dd-mm-YYYY)")
        if type(value) == str:
            msg = jsonify({"Valor UF" : value})
        return msg
    except:
        traceback.print_exc()
        return jsonify('Error al buscar la UF en la Fecha')
        
    
if __name__ == '__main__':
    app.run(debug=True)