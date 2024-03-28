from flask import Flask, jsonify, request
import json
from flask_cors import CORS
from chat import systemMessage


app = Flask(__name__)
CORS(app)


employees = [ { 'id': 1, 'name': 'Ashley' }, { 'id': 2, 'name': 'Kate' }, { 'id': 3, 'name': 'Joe' }]

@app.route("/")
def hello():
    return "Hello, World!"

@app.route('/employees', methods=['GET'])
def get_employees():
    return jsonify(liste = employees)

@app.route('/systemAnswer', methods=['POST'])
def get_info():
    sysMsg, sysQstn = systemMessage(request.json['messageContent'])

    return jsonify({"systemMessage" : sysMsg, "systemQuestion": sysQstn})

if __name__ == '__main__':
    app.run( host = '192.168.1.15', port = 5000 ,debug=True)