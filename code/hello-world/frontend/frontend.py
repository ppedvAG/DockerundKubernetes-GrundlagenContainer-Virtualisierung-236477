from flask import Flask
import socket, os
import requests

app = Flask(__name__)

@app.route('/')
def index():
    
    # backend_response =  requests.get("http://backend:80").text
    backend_response = "Backend is coming later!"
    return f'<html style="background:green;">Hello World, The backend said: {backend_response} </html>'

app.run(host='0.0.0.0', port=80, debug=True)

