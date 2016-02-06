from flask import Flask

from oxford import get_candidates

app = Flask(__name__)

@app.route('/')
def main():
	return "Hello World"

@app.route('/candidates')
def candidates():
	return 'hi'

if __name__ == '__main__':
	app.run()
