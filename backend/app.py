from flask import Flask, request, jsonify
from flask_cors import CORS
from preprocess import preprocess
from week3_main import predict_emotion
from week4_main import fetch_tracks

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.after_request
def add_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "https://vibecheckfrontend.vercel.app"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
    return response
# Mapping emotion labels to Last.fm tags
MOOD_TAGS = {
    "joy": "happy",
    "sadness": "sad",
    "anger": "angry",
    "fear": "scary",
    "love": "love",
    "surprise": "surprise"
}


@app.route("/", methods=["GET"])
def health_check():
    return jsonify({"status": "ok"})


@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()

    if data is None or "text" not in data:
        return jsonify({
            "error": "Request must contain a 'text' field."
        }), 400

    try:
        text = data["text"]

        # Week 2 preprocessing
        cleaned_text = preprocess(text)

        # Week 3 prediction
        emotion, confidence, _ = predict_emotion(text)

        # Convert emotion into Last.fm tag
        tag = MOOD_TAGS.get(emotion, emotion)

        # Week 4 recommendations
        tracks = fetch_tracks(tag)

        return jsonify({
            "emotion": emotion,
            "confidence": confidence,
            "tracks": tracks
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(debug=True)