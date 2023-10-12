"""
Word Occurrences - Prac 05
Estimated: 20 minutes
Actual: 16 minutes
"""


def main():
    """This program will prompt the user to enter text, and then will count the occurrence of each word, then printing
    the word counts."""
    words = input("Text: ")
    word_to_count = count_words(words)
    print_word_counts(word_to_count)


def count_words(text):
    """Count the occurrences of each word in the given text."""
    word_to_count = {}
    words = text.split()

    for word in words:
        try:
            word_to_count[word] += 1
        except KeyError:
            word_to_count[word] = 1

    return word_to_count


def print_word_counts(word_to_count):
    """Print the word counts with aligned formatting."""
    word_max_character_length = (max(len(word) for word in word_to_count))
    sorted_word_to_count = sorted(word_to_count.items())
    for word, count in sorted_word_to_count:
        print(f"{word:>{word_max_character_length}}: {count}")


main()
