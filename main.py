def main():
    book_path = "books/frankenstein.txt"
    contents = read_book(book_path)
    count = word_count(contents)
    letters = letter_count(contents)
    sorted_letters = sort_letters(letters)
    print(f"--- Begin Report of {book_path} ---")
    print(f"{count} words found in the document")
    print(sorted_letters)
    
    
def read_book(book_path):
    with open(book_path) as f:
        return f.read()
    
def word_count(contents):
    words = contents.split()
    return len(words)
    
def letter_count(contents):
    count_dict = {}
    lowercase_contents = contents.lower()
    import string
    letter_list = list(string.ascii_lowercase)
    for letter in letter_list:
        count_dict[letter] = lowercase_contents.count(letter)
    return count_dict

def sort_letters(letters):
    items = letters.items()
    sorted_items = sorted(items, reverse = True, key = lambda item: item[1])
    return dict(sorted_items)
    
main()