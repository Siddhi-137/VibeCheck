from pathlib import Path

import pandas as pd

from preprocess import preprocess


UPLOADED_DATASET_PATH = Path(
    r'C:\Users\siddh\Documents\Codex\2026-06-06\new-chat\outputs\test.txt'
)
LOCAL_DATASET_PATH = Path(__file__).with_name('test.txt')


def get_dataset_path():
    if LOCAL_DATASET_PATH.exists():
        return LOCAL_DATASET_PATH
    return UPLOADED_DATASET_PATH


def load_dataset(path):
    return pd.read_csv(
        path,
        sep=';',
        names=['text', 'label'],
        header=None,
        encoding='utf-8',
    )


def test_preprocess():
    sentences = [
        "I'm SO hyped!!!!",
        "ugh... everything's going wrong",
        "I can't believe this actually worked :)",
        "WHY is my laptop freezing again???",
        "Today was calm, sweet, and surprisingly productive.",
    ]

    print("Preprocessing test sentences")
    print("-" * 40)

    for sentence in sentences:
        print("Original:", sentence)
        print("Tokens:", preprocess(sentence))
        print()


def analyze_dataset():
    df = load_dataset(get_dataset_path())

    print("First 10 rows")
    print("-" * 40)
    print(df.head(10))
    print()

    print("Count of each emotion label")
    print("-" * 40)
    print(df['label'].value_counts())
    print()

    average_word_count = df['text'].apply(lambda text: len(str(text).split())).mean()
    print("Average word count before preprocessing")
    print("-" * 40)
    print(round(average_word_count, 2))
    print()

    print("Joy, sadness, and anger examples after preprocessing")
    print("-" * 40)

    for label in ['joy', 'sadness', 'anger']:
        sentence = df[df['label'] == label].iloc[0]['text']
        print("Label:", label)
        print("Original:", sentence)
        print("Tokens:", preprocess(sentence))
        print()


def main():
    test_preprocess()
    analyze_dataset()


if __name__ == '__main__':
    main()
