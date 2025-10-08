# Delete the Book instance

book_to_delete = Book.objects.get(title="Nineteen Eighty-Four")
book_to_delete.delete()

Book.objects.all()

# Expected output:
# <QuerySet []>
