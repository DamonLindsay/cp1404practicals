"""
Word Occurrences - Prac 05
Estimated: 20 minutes
Actual: 16 minutes
"""
word_to_count = {}

words = input("Text: ").split()

for word in words:
    try:
        word_to_count[word] += 1
    except KeyError:
        word_to_count[word] = 1

word_max_character_length = (max(len(word) for word in word_to_count))
sorted_word_to_count = sorted(word_to_count.items())
for word, count in sorted_word_to_count:
    print(f"{word:>{word_max_character_length}}: {count}")
