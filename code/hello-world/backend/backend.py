from flask import Flask
import socket, os

hostname = os.uname()[1]
ips = socket.gethostbyname_ex(hostname)[2]


app = Flask(__name__)

@app.route('/')
def index():
    return { "ip": str(ips), "username": "root" }

app.run(host='0.0.0.0', port=80, debug=True)

