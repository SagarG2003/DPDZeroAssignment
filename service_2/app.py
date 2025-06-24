# service_2/app.py
from flask import Flask, jsonify
from asgiref.wsgi import WsgiToAsgi

app = Flask(__name__)

@app.route("/ping")
def ping():
    return jsonify(status="ok", service="2")

@app.route("/hello")
def hello():
    return jsonify(message="Hello from Service 2")

# Wrap Flask app with ASGI adapter
asgi_app = WsgiToAsgi(app)
