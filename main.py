def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = word_count(text)
    char_num_list = per_char_count(text)
    report(char_num_list)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def word_count(text):
    words = text.split()
    return len(words)      
    
def per_char_count(text):
    characters = {}
    text_lower = text.lower()
    char_list = list(text_lower)
    for i in char_list:
        if i in characters:
            characters[i] += 1
        else:
            characters[i] = 1
                
    return characters

def report(char_num_list):
    for char in char_num_list:
        if char.isalpha() == True:
            print(f"The '{char}' character was found {char_num_list[char]} times")


main()