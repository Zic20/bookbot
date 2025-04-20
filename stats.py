def get_word_count(content):
    return len(content.split())


def get_character_count(content):
    counter_dict = {}
    characters_list = list(content.lower())
    characters = set(characters_list)
    
    for char in characters:
        counter_dict[char] = content.lower().count(char)
        
    return counter_dict

def sort_dict(counter_dict):
    char_list = []
    for key in counter_dict:
        char_list.append({"char":key,"value":counter_dict[key]})
        
    char_list.sort(reverse=True,key=sort_on)
    return char_list
        

def sort_on(dict):
    return dict["value"]