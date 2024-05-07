def main():
    book_path = "books/frankenstein.txt"
    contents = read_book(book_path)
    count = word_count(contents)
    print(letter_count(contents))
    
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
    
main()