def get_num_words(book_content):
    words = book_content.split()
    return len(words)

def get_num_characters(book_content):
    lowercase_content = book_content.lower()
    character_dict = {}
    for character in lowercase_content:
        if character in character_dict:
            character_dict[character] += 1
        else:
            character_dict[character] = 1
    return character_dict

def sort_on(dict):
    return dict["count"]

def sort_num_characters(char_dict):
    char_list = []
    for char, count in char_dict.items():
        char_list.append({'character': char, 'count': count})
    
    char_list.sort(reverse=True, key=sort_on)
    return char_list


