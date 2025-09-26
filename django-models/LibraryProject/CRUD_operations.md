# CRUD Operations for Book Model

## Create
from bookshelf.models import Book

book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book
# Expected output:
# <Book: 1984>

---

## Retrieve
from bookshelf.models import Book

book = Book.objects.get(title="1984")
book.title
book.author
book.publication_year
# Expected output:
# '1984'
# 'George Orwell'
# 1949

---

## Update
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()

book.title
# Expected output:
# 'Nineteen Eighty-Four'

---

## Delete
book_to_delete = Book.objects.get(title="Nineteen Eighty-Four")
book_to_delete.delete()

Book.objects.all()
# Expected output:
# <QuerySet []>
