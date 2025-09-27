import django
import os

# تهيئة Django عشان نقدر نستخدم الموديلز من سكريبت خارجي
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationships.models import Author, Book, Library, Librarian

# 1️⃣ كل الكتب بتاعة مؤلف معين
author_name = "John Doe"  # غيّري الاسم على حسب اللي عندك
books_by_author = Book.objects.filter(author__name=author_name)
print(f"Books by {author_name}:")
for book in books_by_author:
    print(book.title)

# 2️⃣ كل الكتب في مكتبة معينة
library_name = "Central Library"  # غيّري الاسم على حسب المكتبة
library = Library.objects.get(name=library_name)
print(f"\nBooks in {library.name}:")
for book in library.books.all():
    print(book.title)

# 3️⃣ أمين المكتبة لمكتبة معينة
librarian = Librarian.objects.get(library=library)
print(f"\nLibrarian for {library.name}: {librarian.name}")
