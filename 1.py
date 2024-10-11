library = {

}


def add_book(title, author, year):
    library[title] = {
        'author': author,
        'year': year,
        'available': True,
        'borrower': None
    }


def borrow_book(title, borrower):
    if title in library and library[title]['available'] == True:
        library[title]['available'] = False
        library[title]['borrower'] = borrower
    else:
        print('You can\'t borrower this book')


def return_book(title):
    if title in library:
        library[title]['available'] = True
        library[title]['borrower'] = False


def search_books_by_author(author):
    books = [book for book in library.values() if book['author'].lower() == author.lower()]
    print(books)


add_book('Title', 'Author', 2024)
print(library)

borrow_book('Title', 'Borrower')
print(library)

return_book('Title')
print(library)

search_books_by_author('Author')
