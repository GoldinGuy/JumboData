from flask import request
import json
from . import backend
from . import app


@app.route("/latest_videos")
def videos():
    page_token = request.args.get("page_token")
    return json.dumps(backend.fetch_youtube_latest_uploads(page_token))


# @app.route("/gameplay")
# def gameplay():
#     page_token = request.args.get("page_token")
#     return json.dumps(backend.fetch_youtube_gameplay(page_token))
#
#
# @app.route("/popular")
# def popular_videos():
#     page_token = request.args.get("page_token")
#     return json.dumps(backend.fetch_youtube_popular(page_token))
