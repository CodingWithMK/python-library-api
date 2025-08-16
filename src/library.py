from book import Book

class Library(store_path="library.json"):
    def __init__(self, categories: str, books: Book):
        self.categories = categories
        self.books = Book

    