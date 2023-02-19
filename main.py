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
        "id": uuid.uuid4().hex,
        "title": '2k21',
        "genre": 'Sports',
        "played": "Yes"
    },
    {
        "id": uuid.uuid4().hex,
        "title": 'Evil Within',
        "genre": 'Horror',
        "played": "No"
    },
    {
        "id": uuid.uuid4().hex,
        "title": 'The Last of Us',
        "genre": 'Horror',
        "played": "Yes"
    },
    {
        "id": uuid.uuid4().hex,
        "title": 'Days Gone',
        "genre": 'Horror/Survival',
        "played": "No"
    },
    {
        "id": uuid.uuid4().hex,
        "title": 'Mario',
        "genre": 'Retro',
        "played": "Yes"
    },
    {
        "id": uuid.uuid4().hex,
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


# The PUT and DELETE route handler
@app.route('/games/<game_id>', methods=['PUT', 'DELETE'])
def single_game(game_id):
    print('xa', request.args.get('game_id'))
    response_object = {'status': 'success'}
    if request.method == "PUT":
        post_data = request.get_json()
        remove_game(game_id)
        GAMES.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'genre': post_data.get('genre'),
            'played': post_data.get('played')
        })
        response_object['message'] = 'Game Updated!'
    if request.method == "DELETE":
        remove_game(game_id)
        response_object['message'] = 'Game removed!'
    return jsonify(response_object)


# Removing the game to update / delete
def remove_game(game_id):
    for game in GAMES:
        print(game)
        if game['id'] == game_id:
            GAMES.remove(game)
            return True
    return False


if __name__ == "__main__":
    app.run(debug=True, port=8000)
