import os
import json
import pylast

# ============================
# Last.fm Authentication
# ============================

def get_lastfm_client():
    network = pylast.LastFMNetwork(
        api_key=os.environ["LASTFM_API_KEY"],
        api_secret=os.environ["LASTFM_API_SECRET"]
    )
    print("Last.fm connected successfully")
    return network


# ============================
# Fetch Tracks
# ============================

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


# ============================
# Test All 6 Moods
# ============================

mood_tags = {
    "joy": "happy",
    "sadness": "sad",
    "anger": "angry",
    "fear": "scary",
    "love": "love",
    "surprise": "surprise"
}

all_results = {}

for emotion, tag in mood_tags.items():

    print("\n" + "=" * 60)
    print(f"Emotion : {emotion}")
    print("=" * 60)

    tracks = fetch_tracks(tag)

    all_results[emotion] = tracks

    for i, track in enumerate(tracks, start=1):
        print(f"{i}. Song        : {track['song']}")
        print(f"   Artist      : {track['artist']}")
        print(f"   Cover Image : {track['cover_image']}")
        print(f"   URL         : {track['url']}")
        print()


# ============================
# Save JSON
# ============================

with open("lastfm_results.json", "w", encoding="utf-8") as f:
    json.dump(all_results, f, indent=4)

print("\nSaved to lastfm_results.json")