def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    text = text.lower()  # Convert all characters to lowercase
    character_counts = {}

    for char in text:
        if char in character_counts:
            character_counts[char] += 1
        else:
            character_counts[char] = 1

    return character_counts

def sort_character_counts(char_counts):
    sorted_chars = []

    for char, count in char_counts.items():
        if char.isalpha():  # Only include alphabetic characters
            sorted_chars.append({"char": char, "num": count})

    # Sort by count (descending)
    sorted_chars.sort(key=lambda x: x["num"], reverse=True)

    return sorted_chars