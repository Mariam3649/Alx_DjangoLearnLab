
CRUD Operations for Book model
Create
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book
Expected:

<Book: 1984>
Retrieve
Book.objects.all()
b = Book.objects.get(title="1984")
b.title, b.author, b.publication_year
Expected:

<QuerySet [<Book: 1984>]>
('1984', 'George Orwell', 1949)
Update
b.title = "Nineteen Eighty-Four"
b.save()
Book.objects.get(pk=b.pk).title
Expected:

'Nineteen Eighty-Four'
Delete
b.delete()
list(Book.objects.all())
Expected:

(1, {'bookshelf.Book': 1})
[]
