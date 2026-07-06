MOOD_WORDS = [
    "happy",
    "sad",
    "stressed",
    "hyped",
    "calm",
    "angry",
    "excited",
    "nervous",
    "tired",
    "hopeful",
]


def clean_text(text):
    cleaned_characters = []

    for character in text.lower():
        if character.isalnum() or character.isspace():
            cleaned_characters.append(character)
        else:
            cleaned_characters.append(" ")

    return " ".join("".join(cleaned_characters).split())


def count_words(text):
    cleaned_text = clean_text(text)
    word_counts = {}

    for word in cleaned_text.split():
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    return word_counts


def check_mood_words(sentence):
    words = count_words(sentence)
    found_mood_words = []

    for mood_word in MOOD_WORDS:
        if mood_word in words:
            found_mood_words.append(mood_word)

    if found_mood_words:
        print(", ".join(found_mood_words))
    else:
        print("None")

    return found_mood_words


def top_5_words(text):
    word_counts = count_words(text)
    sorted_words = sorted(word_counts.items(), key=lambda item: (-item[1], item[0]))
    top_words = sorted_words[:5]

    if top_words:
        for word, count in top_words:
            print(f"{word}: {count}")
    else:
        print("No words found")

    return top_words


def test_clean_text():
    sample_sentences = [
        "I am HAPPY, happy, and hopeful!",
        "Wait... are you stressed?",
        "Calm minds, clear plans.",
    ]

    print("CLEAN TEXT TESTS")
    for sentence in sample_sentences:
        print(f"Original: {sentence}")
        print(f"Cleaned:  {clean_text(sentence)}")
    print()


def analyse_sentences_from_file(file_name):
    with open(file_name, "r", encoding="utf-8") as sentence_file:
        sentences = sentence_file.readlines()

    print("MOOD WORD ANALYSIS")
    for number, sentence in enumerate(sentences, start=1):
        sentence = sentence.strip()

        if not sentence:
            continue

        print(f"\nSentence {number}: {sentence}")
        print(f"Cleaned version: {clean_text(sentence)}")
        print("Mood words found:")
        check_mood_words(sentence)
        print("Top 5 most frequent words:")
        top_5_words(sentence)


def main():
    test_clean_text()
    analyse_sentences_from_file("test_sentences.txt")


if __name__ == "__main__":
    main()
