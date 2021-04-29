from flask import Flask, request, render_template, url_for, redirect, jsonify
from flask_restful import Api, Resource, reqparse
import csv

app = Flask(__name__)
api = Api(app)
app.config['JSON_SORT_KEYS'] = False

@app.route('/', methods=['GET'])
def index():
    welcome = "please provide arguments in the following format\n
    /icao_to_iata/<ICAO CODE>\n
    or\n
    /iata_to_icao/<IATA CODE>"
    return welcome

@app.route('/icao_to_iata/<icao>', methods=['GET'])
def IcaoToIata(icao):
    csv_file = csv.reader(open('./icao_iata.csv', 'r'))

    #find the value in the relevant csv and return an IATA code
    if len(icao) == 4:
        for row in csv_file:
            if icao in row[0]:
                iata = ''.join(row)
                iata = iata[5:8]

    else:
        iata="error"
        icao="this is not a valid 4-letter airport code"
    return jsonify({icao: iata})

@app.route('/iata_to_icao/<iata>', methods=['GET'])
def IataToIcao(iata):
    csv_file = csv.reader(open('./iata_icao.csv', 'r'))
    #find the value in the relevant csv and return an ICAO code
    if len(iata)==3:
        for row in csv_file:
            if iata in row[0]:
                icao = ''.join(row)
                icao = icao[4:8]
    else:
        iata = "this is not a valid 3 letter airport code"
        icao = "error"

    return jsonify({iata: icao})

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')
