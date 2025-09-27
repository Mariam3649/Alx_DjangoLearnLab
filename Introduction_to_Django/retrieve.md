# Retrieve

**Command**
```python
from bookshelf.models import Book
Book.objects.all()
b = Book.objects.get(title="1984")
b.title, b.author, b.publication_year

<QuerySet [<Book: 1984>]>
('1984', 'George Orwell', 1949)

<QuerySet [<Book: 1984>]>
('1984', 'George Orwell', 1949)


Retrieved the Book instance and displayed all attributes.
