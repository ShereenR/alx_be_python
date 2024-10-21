class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def show_book(self):
        return f"{self.title} by {self.author}"
    def __str__(self): 
        return f"Book: {self.title} by {self.author}"
class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size
    def show_details(self):
        return f"{self.title} by {self.author}, File Size: {self.file_size} KB"
    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size} KB"
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count
    def show_details(self):
        return f"{self.title} by {self.author}, Page Count: {self.page_count}"
    def __str__(self): 
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"
class Library:
    def __init__(self):
        self.books = []
    def add_book(self, book):
        self.books.append(book)
    def list_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            for book in self.books:
                print(book)  
# مثال على الاستخدام
library = Library()
# إنشاء بعض الكتب وإضافتها إلى المكتبة
book1 = Book("1984", "George Orwell")
ebook1 = EBook("Python Programming", "John Doe", 500)
printbook1 = PrintBook("The Great Gatsby", "F. Scott Fitzgerald", 180)

library.add_book(book1)
library.add_book(ebook1)
library.add_book(printbook1)
# عرض الكتب في المكتبة
library.list_books()
