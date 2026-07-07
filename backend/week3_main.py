from preprocess import preprocess

def predict_emotion(text):
    cleaned_tokens = preprocess(text)
    cleaned_text = " ".join(cleaned_tokens)

    emotion_keywords = {
        "joy": ["happy", "joy", "excited", "great", "amazing", "proud"],
        "sadness": ["sad", "lonely", "miss", "cry", "hopeless", "disappointed"],
        "anger": ["angry", "furious", "mad", "irritated", "annoyed"],
        "fear": ["scared", "afraid", "fear", "terrified", "nervous", "anxious"],
        "love": ["love", "adore", "caring", "warm", "heart"],
        "surprise": ["surprised", "shocked", "unexpected", "wow"],
    }

    scores = {emotion: 0 for emotion in emotion_keywords}

    for emotion, words in emotion_keywords.items():
        for word in words:
            if word in cleaned_text:
                scores[emotion] += 1

    emotion = max(scores, key=scores.get)

    if scores[emotion] == 0:
        emotion = "joy"
        confidence = 0.50
    else:
        confidence = min(0.95, 0.60 + scores[emotion] * 0.15)

    return emotion, confidence, cleaned_text