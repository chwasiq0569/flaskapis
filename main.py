from flask import Flask, jsonify, request
from flask_cors import CORS
import uuid

app = Flask(__name__)

app.config.from_object(__name__)

CORS(app, resources={r"/*": {'origins': '*'}})
CORS(app, resources={r"/*": {'origins': 'http://localhost:8080',
     "allow_headers": "Access-Control-Allow-Origin"}})

GAMES = [
    {
        "title": '2k21',
        "genre": 'Sports',
        "played": "Yes"
    },
    {
        "title": 'Evil Within',
        "genre": 'Horror',
        "played": "No"
    },
    {
        "title": 'The Last of Us',
        "genre": 'Horror',
        "played": "Yes"
    },
    {
        "title": 'Days Gone',
        "genre": 'Horror/Survival',
        "played": "No"
    },
    {
        "title": 'Mario',
        "genre": 'Retro',
        "played": "Yes"
    },
    {
        "title": 'God of War',
        "genre": 'Action',
        "played": "Yes"
    }
]


@app.route('/', methods=['GET'])
def greetings():
    return ('HELLO WORLD')


@app.route("/games", methods=['GET', 'POST'])
def all_games():
    response_object = {'status': 'success'}
    if request.method == "POST":
        GAMES.append({
            'id': uuid.uuid4().hex,
            'title': request.get_json().get('title'),
            'genre': request.get_json().get('genre'),
            'played': request.get_json().get('played')
        })
        response_object['message'] = 'Game Added!'
    else:
        response_object['games'] = GAMES

    return jsonify(response_object)


@app.route("/games/<games_id>", methods=['PUT'])
def single_game(game_id):
    response_object = {'status': 'success'}
    if request.method == "PUT":
        # remove_game(game_id)
        GAMES.append({
            'id': uuid.uuid4().hex,
            'title': request.get_json().get('title'),
            'genre': request.get_json().get('genre'),
            'played': request.get_json().get('played')
        })
        response_object['message'] = 'Game Updated!'

    return jsonify(response_object)


if __name__ == "__main__":
    app.run(debug=True, port=8000)
