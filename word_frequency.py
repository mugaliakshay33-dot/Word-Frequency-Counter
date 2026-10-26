from collections import Counter
from pathlib import Path
import re


def count_words(filename):
    path = Path(filename).expanduser()

    if not path.is_file():
        print("File not found!")
        return

    try:
        text = path.read_text(encoding="utf-8")

        words = re.findall(
            r"[a-z]+(?:'[a-z]+)?",
            text.lower()
        )

        word_count = Counter(words)

        print("\n===== WORD FREQUENCY ANALYSIS =====")

        print("Total Words:", len(words))
        print("Unique Words:", len(word_count))

        print("\nTop 10 Most Frequent Words:")

        for word, count in word_count.most_common(10):
            print(f"{word}: {count}")

    except (OSError, UnicodeError) as error:
        print("Error reading file:", error)


def main():
    print("===== WORD FREQUENCY COUNTER =====")

    filename = input("Enter Text File Path: ").strip()

    count_words(filename)


if __name__ == "__main__":
    main()