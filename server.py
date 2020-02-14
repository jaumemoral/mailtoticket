from flask import Flask, request, send_from_directory
from flask import jsonify
from mailtoticket import processar
import tempfile
import os

app = Flask(__name__)

@app.route("/", methods = ['POST'])
def enviarMailtoticket():
    try:
        # Passem fer un fitxer temporal perque si llegim directament del stream, gunicorn falla
        temp=tempfile.NamedTemporaryFile(delete=False)
        temp.write(request.get_data())    
        filename=temp.name
        temp.close()
        with open(filename,"rb") as f:
            sortida=processar(f)
        os.remove(filename)
        return jsonify({"status":sortida})
    except:
        return jsonify({"status":"ERROR"})

@app.route("/img/<path:path>")
def img(path):
    return send_from_directory('./img', path)
