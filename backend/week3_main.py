import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
HF_CACHE_DIR = Path(os.environ.get("HF_HOME", BASE_DIR / "hf_cache")).resolve()
HF_CACHE_DIR.mkdir(exist_ok=True)

os.environ.setdefault("HF_HOME", str(HF_CACHE_DIR))
os.environ.setdefault("HF_HUB_CACHE", str(HF_CACHE_DIR / "hub"))
os.environ.setdefault("HF_HUB_DISABLE_SYMLINKS_WARNING", "1")
os.environ.setdefault("HF_HUB_DISABLE_XET", "1")

try:
    import torch
    import transformers
    from transformers import pipeline
except ImportError as error:
    raise SystemExit(
        "Missing dependency. Install the required packages first with:\n"
        "python -m pip install -r requirements.txt"
    ) from error

from preprocess import preprocess


MODEL_NAME = "bhadresh-savani/distilbert-base-uncased-emotion"
RESULTS_PATH = BASE_DIR / "results.txt"
MODEL_CACHE_DIR = (
    Path(os.environ["HF_HUB_CACHE"])
    / "models--bhadresh-savani--distilbert-base-uncased-emotion"
)
MODEL_CACHE_DIR.joinpath("blobs").mkdir(parents=True, exist_ok=True)

TEST_SENTENCES = [
    (
        "I feel joyful and excited because my song finally came together.",
        "joy",
    ),
    (
        "Winning the quiz made me happy, proud, and full of energy.",
        "joy",
    ),
    (
        "I feel sad and lonely after saying goodbye to my best friend.",
        "sadness",
    ),
    (
        "The empty room made me feel hopeless and deeply disappointed.",
        "sadness",
    ),
    (
        "I am furious and angry that my work was deleted without warning.",
        "anger",
    ),
    (
        "His rude comment made me irritated, offended, and ready to shout.",
        "anger",
    ),
    (
        "I am terrified and afraid of walking alone through the dark street.",
        "fear",
    ),
    (
        "I adore my partner and love them with my whole heart.",
        "love",
    ),
    (
        "Her gentle message made me feel loved, cared for, and warm.",
        "love",
    ),
    (
        "I was shocked and surprised when everyone planned a party for me.",
        "surprise",
    ),
]

classifier = None

def get_classifier():
    global classifier
    if classifier is None:
        classifier = pipeline("text-classification", model=MODEL_NAME)
    return classifier

def predict_emotion(text):
    """
    Clean text with the Week 2 preprocess() function and predict its emotion.

    Returns the predicted label, confidence score, and cleaned text.
    """
    cleaned_tokens = preprocess(text)
    cleaned_text = " ".join(cleaned_tokens)

    if not cleaned_text:
        cleaned_text = str(text)

    prediction = get_classifier()(cleaned_text)[0]
    return prediction["label"], prediction["score"], cleaned_text


def run_tests():
    correct_count = 0
    result_lines = [
        "Week 3 Emotion Detector Results",
        "=" * 32,
        f"transformers version: {transformers.__version__}",
        f"torch version: {torch.__version__}",
        f"model: {MODEL_NAME}",
        "",
    ]

    print("Week 3 Emotion Detector")
    print("-" * 40)
    print("Model:", MODEL_NAME)
    print("Transformers version:", transformers.__version__)
    print("Torch version:", torch.__version__)
    print()

    for index, (sentence, expected_label) in enumerate(TEST_SENTENCES, start=1):
        predicted_label, confidence, cleaned_text = predict_emotion(sentence)
        is_correct = predicted_label == expected_label
        correct_count += int(is_correct)

        print(f"{index}. {sentence}")
        print("Cleaned:", cleaned_text)
        print("Expected:", expected_label)
        print("Predicted:", predicted_label)
        print("Confidence:", round(confidence, 4))
        print("Correct:", "yes" if is_correct else "no")
        print()

        result_lines.extend(
            [
                f"{index}. {sentence}",
                f"Cleaned: {cleaned_text}",
                f"Expected: {expected_label}",
                f"Predicted: {predicted_label}",
                f"Confidence: {confidence:.4f}",
                f"Correct: {'yes' if is_correct else 'no'}",
                "",
            ]
        )

    total_count = len(TEST_SENTENCES)
    summary = f"Summary: {correct_count} out of {total_count} predictions matched the expected labels."
    print(summary)
    result_lines.append(summary)

    RESULTS_PATH.write_text("\n".join(result_lines), encoding="utf-8")
    print(f"Saved results to {RESULTS_PATH}")


def main():
    run_tests()


if __name__ == "__main__":
    main()
