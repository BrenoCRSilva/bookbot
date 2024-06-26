def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_char = get_num_chars(text)
    sorted_list = get_sorted_list(num_char)
    
    print("--- Begin report of books/frankenstein.txt ---\n", f"{num_words} words found in the document\n")
    for char, count in sorted_list:
        print(f"The '{char}' character was found {count} times.")
    print("--- End report ---")

def get_num_words(text):
    return len(text.split())

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_chars(text):
    char_dict = {}
    char_list = ["a", "b", "c", "d", "e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    for char in char_list:
        count = text.lower().count(char)
        char_dict[char] = count
    return char_dict
        
def get_sorted_list(num_char):
    return sorted(num_char.items(), key=lambda x: x[1], reverse=True)

main()