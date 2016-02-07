from flask import Flask, request
from flask_sockets import Sockets
from gevent import pywsgi
from geventwebsocket.handler import WebSocketHandler
import json
import yaml

from graph import *
print('server running...')

app = Flask(__name__)
app.debug = True
sockets = Sockets(app)

@app.route('/')
def main():
    return "Hello World"

@sockets.route('/api')
def echo_socket(ws):
    while not ws.closed:
        message = ws.receive()
        message = yaml.safe_load(message)
        # event is a string
        # data is a string
        # limit is an optional integer
        if (message["event"] == 'haiku'):
            print('haiku')
            data = message['data']
            response = complete_haiku(data)
            ws.send(json.dumps(response))
        elif message["event"] == 'line':
            print('line')
            data = message['data']
            limit = message['length']
            print(data, limit)
            response = complete_line(data, limit)
            print(response)
            ws.send(json.dumps(response))
        else:
            ws.send("fuck this shit")

if __name__ == '__main__':
    server = pywsgi.WSGIServer(('', 5000), app, handler_class=WebSocketHandler)
    server.serve_forever()
