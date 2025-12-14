from book import Book
from member import Member

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    def add_book(self, book):
        self.books[book.book_id] = book

    def add_member(self, member):
        self.members[member.member_id] = member

    def show_books(self):
        for book in self.books.values():
            print(book)

    def issue_book(self, book_id, member_id):
        book = self.books.get(book_id)
        member = self.members.get(member_id)

        if not book or not member:
            print("Invalid ID")
            return

        if book.is_issued:
            print("Book already issued")
            return

        book.is_issued = True
        member.issued_books.append(book)

    def return_book(self, book_id, member_id):
        member = self.members.get(member_id)
        if not member:
            print("Invalid member")
            return

        for book in member.issued_books:
            if book.book_id == book_id:
                book.is_issued = False
                member.issued_books.remove(book)
                return
