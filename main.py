from flask import Flask, request, render_template, url_for, redirect, jsonify
from flask_restful import Api, Resource, reqparse
from converter import airport

app = Flask(__name__)
api = Api(app)
app.config['JSON_SORT_KEYS'] = False

@app.route('/<icao>', methods=['GET'])
def convert(icao):
    iata = airport(icao)
    #return iata
    return jsonify({icao: iata})

if __name__ == "__main__":
    app.run(debug=True)