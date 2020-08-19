from flask import request
import json
from . import backend
from . import app


@app.route("/latest_videos")
def videos():
    page_token = request.args.get("page_token")
    return json.dumps(backend.fetch_youtube_latest_uploads(page_token))


@app.route("/gameplay")
def gameplay():
    page_token = request.args.get("page_token")
    return json.dumps(backend.fetch_youtube_gameplay(page_token))


@app.route("/popular")
def popular_videos():
    page_token = request.args.get("page_token")
    return json.dumps(backend.fetch_youtube_popular(page_token))


@app.route("/deck_techs")
def deck_techs():
    page = int(request.args.get("page", 0))
    return json.dumps(backend.retrieve_decks(type="deckTechs", page=page))


@app.route("/my_decks")
def my_decks():
    page = int(request.args.get("page", 0))
    return json.dumps(backend.retrieve_decks(type="myDecks", page=page))

@app.route("/misc")
def misc():
    page = int(request.args.get("page", 0))
    return json.dumps(backend.retrieve_decks(type="misc", page=page))

@app.route("/all_decks")
def all_decks():
    page = int(request.args.get("page", 0))
    return json.dumps(backend.retrieve_decks(type="all", page=page))
