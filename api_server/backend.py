import os
import functools
import itertools
import json

import googleapiclient.discovery
import googleapiclient.errors

from . import mc, youtube, YOUTUBE_CHANNEL, YOUTUBE_API_KEY

# TODO: is it possible to remove these globals?
latest_response = {}
# gameplay_response = {}
# popular_response = {}

global_counter = 0


def cb(c, response):
    if latest_response.get(c) is None:
        latest_response[c] = []
    latest_response[c].append(response)


def fetch_youtube_latest_uploads(page_token=None):
    youtube_page_cached = mc.get("LATEST_PAGE_" + str(page_token))
    if youtube_page_cached is not None:
        return json.loads(youtube_page_cached)

    global global_counter

    this_counter = global_counter
    global_counter += 1

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

    batch = youtube.new_batch_http_request()
    for playlist in playlists:
        batch.add(
            youtube.playlistItems().list(
                part="snippet", playlistId=playlist, maxResults=30, pageToken=page_token
            ),
            callback=functools.partial(cb, this_counter),
        )
    batch.execute()

    data = {
        "kind": "youtube",
        "nextPageToken": latest_response[this_counter][0]["nextPageToken"],
        "items": list(
            itertools.chain.from_iterable(
                map(lambda x: x["items"],
                    latest_response[this_counter])
            )
        ),
    }
    mc.add("LATEST_PAGE_" + str(page_token), json.dumps(data), time=60 * 30)
    del latest_response[this_counter]

    return data

#
# def fetch_youtube_gameplay(page_token=None):
#     gameplay_page_cached = mc.get("GAMEPLAY_PAGE_" + str(page_token))
#     if gameplay_page_cached is not None:
#         return json.loads(gameplay_page_cached)
#
#     global global_counter
#
#     this_counter = global_counter
#     global_counter += 1
#
#     batch = youtube.new_batch_http_request()
#     batch.add(
#         youtube.playlistItems().list(
#             part="snippet", playlistId='PL0VGXNIrhFXhZy_AAbsnKyZdRFJmabKzQ', maxResults=15, pageToken=page_token
#         ),
#         callback=functools.partial(cb, this_counter),
#     )
#
#     data = {
#         "kind": "youtube",
#         "nextPageToken": gameplay_response[this_counter][0]["nextPageToken"],
#         "items": list(
#             itertools.chain.from_iterable(
#                 map(lambda x: x["items"],
#                     gameplay_response[this_counter])
#             )
#         ),
#     }
#     mc.add("GAMEPLAY_PAGE_" + str(page_token), json.dumps(data), time=60 * 30)
#     del gameplay_response[this_counter]
#
#     return data
#
#
# def fetch_youtube_popular(page_token=None):
#     popular_page_cached = mc.get("POPULAR_PAGE_" + str(page_token))
#     if popular_page_cached is not None:
#         return json.loads(popular_page_cached)
#
#     global global_counter
#
#     this_counter = global_counter
#     global_counter += 1
#
#     batch = youtube.new_batch_http_request()
#     batch.add(
#         youtube.playlistItems().list(
#             part="snippet", playlistId='', maxResults=2, pageToken=page_token
#         ),
#         callback=functools.partial(cb, this_counter),
#     )
#     data = {
#         "kind": "youtube",
#         "nextPageToken": global_youtube_response[this_counter][0]["nextPageToken"],
#         "items": list(
#             itertools.chain.from_iterable(
#                 map(lambda x: x["items"],
#                     global_youtube_response[this_counter])
#             )
#         ),
#     }
#     mc.add("POPULAR_PAGE_" + str(page_token), json.dumps(data), time=60 * 30)
#     del global_youtube_response[this_counter]
#
#     return data
