def total_word_count(book_text):
    return len(book_text.split())

def letter_count (letters):
    book_dict = {}
    for char in letters:
        char = char.lower()
        if not char.isalpha():
            continue
        if char in book_dict:
            book_dict[char] += 1
        else:
            book_dict[char] = 1
    return book_dict

def sort_character_counts(char_counts):
    sorted_chars = sorted(char_counts.items(), key=lambda item: item [1], reverse=True)
    character_dict = []
    for char, count in sorted_chars:
        char_info = {"char": char, "num":count}
        character_dict.append(char_info)
    return character_dict