['main.py', 'books/mobydick.txt', 'books/frankenstein.txt', 'books/prideandprejudice.txt' ]

import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(path_to_books):
    with open(path_to_books) as f:
        file_contents = f.read()
    return(file_contents)



from stats import total_word_count

from stats import letter_count

from stats import sort_character_counts

def main():
    
    book_path = sys.argv[1]
    book_contents = get_book_text(book_path)
    num_words = total_word_count(book_contents)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    char_counts = letter_count(book_contents)
    #i removedprint(char_counts)

    sorted_char_list = sort_character_counts(char_counts)
    #i removed print(sorted_char_list)

    for item in sorted_char_list:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")



main ()

