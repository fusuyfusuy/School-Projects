from flask import Flask, request, Response
from flask_restful import Resource, Api
import csv
import json
import AHP
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/', methods = ['GET', 'POST', 'DELETE'])
def bicycles():
    if(request.method=='GET'):
        return 'use Post'
    elif(request.method=='POST'):
        data = request.json
        return json.dumps(AHP.runAHP(data))

if __name__ == '__main__':
    app.run(debug=True)
