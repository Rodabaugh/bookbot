def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_contents(book_path)
    word_count = get_word_count(book_text)
    print(f"The book contains {word_count} words.")
    sorted_letter_count = sort_letter_count(get_letter_count(book_text))
    print(sorted_letter_count)

def get_book_contents(book_path):
    with open(book_path) as book:
        return book.read()

def get_word_count(book_text):
    words = book_text.split()
    return len(words)

def get_letter_count(book_text):
    letter_count = {}
    book_text = book_text.lower()
    for i in range(0, len(book_text)):
        if book_text[i] in letter_count:
            letter_count[book_text[i]] += 1
        else:
            letter_count[book_text[i]] = 1
    return letter_count

def sort_letter_count(letter_count):
    report = []
    for char in letter_count:
        if char.isalpha():
            report.append({"letter": char, "count": letter_count[char]})
    report.sort(reverse=True, key=sort_on)
    return report

def sort_on(dict):
    return dict["count"]

main()