import sys
from stats import word_count, character_count, sort_character_count 

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def print_results(total_words, filepath, char_info): #easier for me to format the standard output
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")
    for letter_info in char_info:
        print(f"{letter_info['char']}: {letter_info['num']}")
    print("============= END ===============")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    text_wall = get_book_text(filepath) # returns string
    amount_words = word_count(text_wall) # returns int
    letter_count = character_count(text_wall) # returns dictionary
    sorted_char_count = sort_character_count(letter_count) # returns list of dict
    print_results(amount_words, filepath, sorted_char_count)

main()