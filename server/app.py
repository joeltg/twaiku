from flask import Flask
from flask_sockets import Sockets
from gevent import pywsgi
from geventwebsocket.handler import WebSocketHandler

app = Flask(__name__)
app.debug = True
sockets = Sockets(app)


@app.route('/')
def main():
    return "Hello World"


@app.route('/candidates')
def candidates():
    return 'hi'


@sockets.route('/echo')
def echo_socket(ws):
    while not ws.closed:
        message = ws.receive()
        ws.send("fuck this shit")


if __name__ == '__main__':
    server = pywsgi.WSGIServer(('', 5000), app, handler_class=WebSocketHandler)
    server.serve_forever()
