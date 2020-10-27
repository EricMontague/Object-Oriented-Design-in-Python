class Author:
    def __init__(self, author_id, name, books):
        self._author_id = author_id
        self._name = name
        self._books = books

    @property
    def author_id(self):
        return self._author_id

    @property
    def name(self):
        return self._name

    @property
    def books(self):
        return self._books

    def add_book(self, book):
        self._books.append(book)

