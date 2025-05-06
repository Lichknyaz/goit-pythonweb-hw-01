from abc import ABC, abstractmethod


class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"


class LibraryInterface(ABC):

    @abstractmethod
    def add_book(self, title, author, year):
        pass

    @abstractmethod
    def remove_book(self, title):
        pass

    @abstractmethod
    def show_books(self):
        pass


class Library(LibraryInterface):
    def __init__(self):
        self.books: list[Book] = []

    def add_book(self, title, author, year):
        self.books.append(Book(title, author, year))

    def remove_book(self, title):
        self.books = [book for book in self.books if book.title != title]

    def show_books(self):
        return self.books


class LibraryManager:
    def __init__(self, library: LibraryInterface):
        self.library = library

    def add_book(self, title: str, author: str, year: str):
        self.library.add_book(title, author, year)

    def remove_book(self, title: str):
        self.library.remove_book(title)

    def show_books(self):
        books = self.library.show_books()
        if not books:
            print("Library is empty.")
        for book in books:
            print(book)


def main():
    library = Library()
    manager = LibraryManager(library)

    while True:
        command = input("Enter command (add, remove, show, exit): ").strip().lower()

        match command:
            case "add":
                title = input("Enter book title: ").strip()
                author = input("Enter book author: ").strip()
                year = input("Enter book year: ").strip()
                manager.add_book(title, author, year)
            case "remove":
                title = input("Enter book title to remove: ").strip()
                manager.remove_book(title)
            case "show":
                manager.show_books()
            case "exit":
                break
            case _:
                print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
