from flask import Flask, request
from flask_sockets import Sockets
from gevent import pywsgi
from geventwebsocket.handler import WebSocketHandler
import json
import yaml
import random

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
            auto = [a for a in auto_complete(word.lower()) if does_word_exist(a)]
            random.shuffle(auto)
            if does_word_exist(word):
                total += count_syllables_word(word)
            else:
                total += count_syllables_word(auto[0])
            path.append([word.lower(), total, auto])
        if (message["event"] == 'haiku'):
            print('haiku')
            response = complete_haiku(path)
            print path_to_string(path)
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
