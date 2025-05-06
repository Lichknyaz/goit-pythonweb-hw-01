from abc import ABC, abstractmethod
import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")


class Book:
    def __init__(self, title, author, year) -> None:
        self.title = title
        self.author = author
        self.year = year

    def __str__(self) -> str:
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"


class LibraryInterface(ABC):

    @abstractmethod
    def add_book(self, title, author, year) -> None:
        pass

    @abstractmethod
    def remove_book(self, title) -> None:
        pass

    @abstractmethod
    def show_books(self) -> list[Book]:
        pass


class Library(LibraryInterface):
    def __init__(self) -> None:
        self.books: list[Book] = []

    def add_book(self, title, author, year) -> None:
        self.books.append(Book(title, author, year))

    def remove_book(self, title) -> None:
        self.books = [book for book in self.books if book.title != title]

    def show_books(self) -> list[Book]:
        return self.books


class LibraryManager:
    def __init__(self, library: LibraryInterface) -> None:
        self.library = library

    def add_book(self, title: str, author: str, year: str) -> None:
        self.library.add_book(title, author, year)

    def remove_book(self, title: str) -> None:
        self.library.remove_book(title)

    def show_books(self) -> None:
        books: list[Book] = self.library.show_books()
        if not books:
            logging.info("Library is empty.")
        for book in books:
            logging.info(book)


def main():
    library: LibraryInterface = Library()
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
                logging.info("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
