from flask import Flask, request, send_from_directory
from flask import jsonify
from mailtoticket import processar

app = Flask(__name__)

@app.route("/", methods = ['POST'])
def enviarMailtoticket():
    sortida=processar(request.stream)
    return jsonify({"status":sortida})

@app.route("/img/<path:path>")
def img(path):
    return send_from_directory('./img', path)
