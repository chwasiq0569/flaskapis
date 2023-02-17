from flask import Flask, jsonify
from flask_cors import CORS


app = Flask(__name__)

app.config.from_object(__name__)

CORS(app, resources={r"/*": {'origins': '*'}})
CORS(app, resources={r"/*": {'origins': 'http://localhost:8080',
     "allow_headers": "Access-Control-Allow-Origin"}})


@app.route('/', methods=['GET'])
def greetings():
    return ('HELLO WORLD')


if __name__ == "__main__":
    app.run(debug=True, port=8000)
