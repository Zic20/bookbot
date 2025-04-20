from stats import get_word_count,get_character_count,sort_dict
import sys

def get_book_text(filepath):
    file_contents = ""
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    content = get_book_text(book)
    print("----------- Word Count ----------")
    num_words = get_word_count(content)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    sorted_dict = sort_dict(get_character_count(content))
    for item in sorted_dict:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["value"]}")
            
    print("============= END ===============")
    
    
    
    


main()