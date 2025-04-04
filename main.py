import sys
from stats import get_num_words, get_num_characters, sort_num_characters

def get_book_text(file_path):
    file_content = "nothing happened"
    with open(file_path) as f:
        file_contents = f.read()

    return file_contents


def main():
    if(len(sys.argv) < 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    content = get_book_text(filepath)
    num_words = get_num_words(content)
    char_dict = get_num_characters(content)
    sorted_list = sort_num_characters(char_dict)
   
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_list:
         char = item["character"]
         count = item["count"]
         if char.isalpha():
             print(f"{char}: {count}")
    print("============= END ===============")

main()