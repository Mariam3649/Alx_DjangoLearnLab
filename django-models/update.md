
Update
Command

from bookshelf.models import Book
b = Book.objects.get(title="1984")
b.title = "Nineteen Eighty-Four"
b.save()
Book.objects.get(pk=b.pk).title
Expected output

'Nineteen Eighty-Four'
Comment
Updated the title from "1984" to "Nineteen Eighty-Four" and saved the changes.
