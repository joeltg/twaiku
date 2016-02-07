from flask import Flask
from flask_sockets import Sockets
from gevent import pywsgi
from geventwebsocket.handler import WebSocketHandler
import json
import yaml

app = Flask(__name__)
app.debug = True
sockets = Sockets(app)

test_message = [
    [{"text":"while","flag": True}, {"text":"the","flag": False}, {"text":"final","flag": False}, {"text":"say","flag": False}],
    [{"text":"crazed","flag": False}, {"text":"monosyllables","flag": False}],
    [{"text":"modesto","flag": False}, {"text":"shallow","flag": False}]
]

@app.route('/')
def main():
    return "Hello World"


@app.route('/candidates')
def candidates():
    return 'hi'


@sockets.route('/twaiku')
def echo_socket(ws):
    while not ws.closed:
        message = ws.receive()
        message = yaml.safe_load(message)
        print message
        if (message["event"] == 'haiku'):
            ws.send(json.dumps(test_message))
        else:
            ws.send("fuck this shit")

if __name__ == '__main__':
    server = pywsgi.WSGIServer(('', 80), app, handler_class=WebSocketHandler)
    server.serve_forever()
