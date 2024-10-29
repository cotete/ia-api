from flask import Flask,request,jsonify
import numpy as np
import pickle


app = Flask(__name__)

with open('modelo','wb'):
    modelo = pickle.load()


@app.route('/prever',methods=['GET'])
def prever():
    parametro1 = float(request.args.get('comp_abd'))
    parametro2 = float(request.args.get('comp_ant'))

    entrada = np.array([{parametro1,parametro2}])
    resultado = modelo.predict(entrada)

    return jsonify({'resultado':resultado})