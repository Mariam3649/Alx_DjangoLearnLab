# Create

**Command**
```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book

<Book: 1984>

from bookshelf.models import Book
Book.objects.all()
b = Book.objects.get(title="1984")
b.title, b.author, b.publication_year

<QuerySet [<Book: 1984>]>
('1984', 'George Orwell', 1949)

from bookshelf.models import Book
b = Book.objects.get(title="1984")
b.title = "Nineteen Eighty-Four"
b.save()
Book.objects.get(pk=b.pk).title

'Nineteen Eighty-Four'

from bookshelf.models import Book
b = Book.objects.get(title="Nineteen Eighty-Four")
b.delete()
list(Book.objects.all())

(1, {'bookshelf.Book': 1})
[]

from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book

<Book: 1984>

Book.objects.all()
b = Book.objects.get(title="1984")
b.title, b.author, b.publication_year

<QuerySet [<Book: 1984>]>
('1984', 'George Orwell', 1949)

b.title = "Nineteen Eighty-Four"
b.save()
Book.objects.get(pk=b.pk).title

'Nineteen Eighty-Four'

b.delete()
list(Book.objects.all())

(1, {'bookshelf.Book': 1})
[]

(1, {'bookshelf.Book': 1})
[]

