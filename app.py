from flask import Flask, request
from flask_sockets import Sockets
from gevent import pywsgi
from geventwebsocket.handler import WebSocketHandler
import json
import yaml

from syllables import does_word_exist
from auto_completion import auto_complete

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
        data = message['data']
        path = []
        total = 0
        for word in data.split(' '):
            total += count_syllables_word(word)
            path.append([word.lower(), total, auto_complete(word.lower())])
        if (message["event"] == 'haiku'):
            print('haiku')
            response = complete_haiku(path)
            print path_to_string(response)
            ws.send(json.dumps(response))
        elif message["event"] == 'line':
            print('line')
            limit = message['length']
            response = complete_line(path, limit)
            ws.send(json.dumps(response))
        else:
            ws.send("fuck this shit")

if __name__ == '__main__':
    server = pywsgi.WSGIServer(('', 5000), app, handler_class=WebSocketHandler)
    server.serve_forever()
