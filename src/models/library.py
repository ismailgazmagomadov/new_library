from book import Book


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, title, author):
        """Добавить книгу"""
        book = Book(title, author)
        self.books.append(book)
        return book

    def find_by_title(self, title):
        """Найти книгу по названию без учёта регистра"""
        if not title:
            return None
        for book in self.books:
            if book.title.lower() == title.strip().lower():
                return book
        return None

    def borrow_book(self, title):
        """Выдать книгу"""
        book = self.find_by_title(title)
        if not book:
            return False

        if book.borrow():
            return True
        return False

    def return_book(self, title):
        """Вернуть книгу в библиотеку"""
        book = self.find_by_title(title)
        if not book:
            return False
        return book.return_book()

    def find_by_author(author: str) -> list[Book]:
        return [book for book in self.books if book.author == author]

    def get_sorted_by_year(self, books, reverse=False) -> list[Book]:
        sorted_list = sorted(books, key=lambda x: x.year, reverse=reverse)
        return sorted_list
