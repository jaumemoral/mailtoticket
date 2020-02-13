from flask import Flask, request
from flask import jsonify
from mailtoticket import processar

app = Flask(__name__)

@app.route("/", methods = ['POST'])
def enviarMailtoticket():
    sortida=processar(request.stream)
    return jsonify({"status":sortida})