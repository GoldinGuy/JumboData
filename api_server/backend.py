import os
import functools
import itertools
import json

import googleapiclient.discovery
import googleapiclient.errors

from . import mc, youtube, YOUTUBE_CHANNEL, YOUTUBE_API_KEY

# TODO: is it possible to remove these globals?
youtube_response = {}
# gameplay_response = {}
# popular_response = {}

global_counter = 0


def getPlaylists():
    youtubeAPI = googleapiclient.discovery.build(
        "youtube", "v3", developerKey=YOUTUBE_API_KEY)

    playlists = []
    try:
        request = youtubeAPI.channels().list(part="contentDetails", id=YOUTUBE_CHANNEL)
        response = request.execute()
        uploads_id = response["items"][0]["contentDetails"]["relatedPlaylists"][
            "uploads"
        ]
    except:
        request = youtubeAPI.channels().list(
            part="contentDetails", forUsername=YOUTUBE_CHANNEL
        )
        response = request.execute()
        uploads_id = response["items"][0]["contentDetails"]["relatedPlaylists"][
            "uploads"
        ]
    playlists.append(uploads_id)
    # print("PLAYLIST_IDS=" + ";".join(playlists))
    return playlists


def cb(c, request_id, response, exception):
    if youtube_response.get(c) is None:
        youtube_response[c] = []
    youtube_response[c].append(response)


def fetch_youtube_latest_uploads(page_token=None):
    youtube_page_cached = mc.get("LATEST_PAGE_" + str(page_token))
    if youtube_page_cached is not None:
        return json.loads(youtube_page_cached)

    global global_counter

    this_counter = global_counter
    global_counter += 1

    batch = youtube.new_batch_http_request()
    for playlist in getPlaylists():
        batch.add(
            youtube.playlistItems().list(
                part="snippet", playlistId=playlist, maxResults=30, pageToken=page_token
            ),
            callback=functools.partial(cb, this_counter),
        )
    batch.execute()

    data = {
        "kind": "youtube",
        "nextPageToken": youtube_response[this_counter][0]["nextPageToken"],
        "items": list(
            itertools.chain.from_iterable(
                map(lambda x: x["items"],
                    youtube_response[this_counter])
            )
        ),
    }
    mc.add("LATEST_PAGE_" + str(page_token), json.dumps(data), time=60 * 30)
    del youtube_response[this_counter]

    return data


def fetch_youtube_gameplay(page_token=None):
    youtube_page_cached = mc.get("GAMEPLAY_PAGE_" + str(page_token))
    if youtube_page_cached is not None:
        return json.loads(youtube_page_cached)

    global global_counter

    this_counter = global_counter
    global_counter += 1

    batch = youtube.new_batch_http_request()
    batch.add(
        youtube.playlistItems().list(
            part="snippet", playlistId='PL0VGXNIrhFXhZy_AAbsnKyZdRFJmabKzQ', maxResults=12, pageToken=page_token
        ),
        callback=functools.partial(cb, this_counter),
    )
    batch.execute()

    data = {
        "kind": "youtube",
        "nextPageToken": youtube_response[this_counter][0]["nextPageToken"],
        "items": list(
            itertools.chain.from_iterable(
                map(lambda x: x["items"],
                    youtube_response[this_counter])
            )
        ),
    }
    mc.add("GAMEPLAY_PAGE_" + str(page_token), json.dumps(data), time=60 * 30)
    del youtube_response[this_counter]
    return data

def fetch_youtube_popular(page_token=None):
    youtube_page_cached = mc.get("POPULAR_PAGE_" + str(page_token))
    if youtube_page_cached is not None:
        return json.loads(youtube_page_cached)

    global global_counter

    this_counter = global_counter
    global_counter += 1

    batch = youtube.new_batch_http_request()
    batch.add(
        request = youtube.search().list(
            part="snippet",
            channelId="UCPqT2ULat4WIzWKqpAAOlIQ",
            maxResults=10,
            order="viewCount"
        ),
        callback=functools.partial(cb, this_counter)
    )
    batch.execute()

    data = {
        "kind": "youtube",
        "nextPageToken": youtube_response[this_counter][0]["nextPageToken"],
        "items": list(
            itertools.chain.from_iterable(
                map(lambda x: x["items"],
                    youtube_response[this_counter])
            )
        ),
    }
    mc.add("POPULAR_PAGE_" + str(page_token), json.dumps(data), time=60 * 30)
    del youtube_response[this_counter]

    return data