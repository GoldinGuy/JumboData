import os

import googleapiclient.discovery
import googleapiclient.errors


API_KEY = 'AIzaSyAIhhqu-7lJmmacYA2Q_gu8jrJJL7YVHWM'
# API_KEY = os.environ["YOUTUBE_API_KEY"]


def main():
    # Channel ID
    channel = 'UCPqT2ULat4WIzWKqpAAOlIQ'

    youtube = googleapiclient.discovery.build(
        "youtube", "v3", developerKey=API_KEY)

    playlists = []
    try:
        request = youtube.channels().list(part="contentDetails", id=channel)
        response = request.execute()
        uploads_id = response["items"][0]["contentDetails"]["relatedPlaylists"][
            "uploads"
        ]
    except:
        request = youtube.channels().list(
            part="contentDetails", forUsername=channel
        )
        response = request.execute()
        uploads_id = response["items"][0]["contentDetails"]["relatedPlaylists"][
            "uploads"
        ]
    playlists.append(uploads_id)

    print("PLAYLIST_IDS=" + ";".join(playlists))


if __name__ == "__main__":
    main()
