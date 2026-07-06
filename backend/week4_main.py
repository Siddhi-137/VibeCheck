import os
import pylast

def get_lastfm_client():
    network = pylast.LastFMNetwork(
        api_key=os.environ["LASTFM_API_KEY"],
        api_secret=os.environ["LASTFM_API_SECRET"]
    )
    return network

def fetch_tracks(mood, limit=5):
    network = get_lastfm_client()

    tag = network.get_tag(mood)
    top_tracks = tag.get_top_tracks(limit=limit)

    results = []

    for item in top_tracks:
        track = item.item

        try:
            cover = track.get_cover_image()
        except:
            cover = None

        results.append({
            "song": track.get_title(),
            "artist": track.get_artist().get_name(),
            "cover_image": cover,
            "url": track.get_url()
        })

    return results