class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    def __repr__(self):
        return f"Book: {self.title} by {self.author}"



class EBook(Book):
    def __init__(self, title, author, file_size: int):
        super().__init__(title, author)
        self.file_size = file_size

    def __repr__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    def __init__(self, title, author, page_count: int):
        super().__init__(title, author)
        self.page_count = page_count

    def __repr__(self):
        return f"PrintBook: {self.title} by {self.author},Page count: {self.page_count}"


class Library:
    def __init__(self):
        self.books = []


    def add_book(self, books):
        self.books.append(books)


    def list_book in self.books:
        for book in self.books:
            print(book.__str__())
