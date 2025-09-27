
Delete
Command

from bookshelf.models import Book
b = Book.objects.get(title="Nineteen Eighty-Four")
b.delete()
list(Book.objects.all())
Expected output

(1, {'bookshelf.Book': 1})
[]
Comment
Deleted the Book instance and confirmed the database is empty.
