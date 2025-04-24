import sys
from stats import *

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]

book_text = get_book_text(book_path)


word_count = count_words(book_text)
char_counts = count_characters(book_text)
sorted_char_counts = sort_character_counts(char_counts)

# Report
print("============ BOOKBOT ============")
print(f"Analyzing book found at {book_path}...")
print("----------- Word Count ----------")
print(f"Found {word_count} total words")
print("--------- Character Count -------")

for item in sorted_char_counts:
    print(f"{item['char']}: {item['num']}")

print("============= END ===============")