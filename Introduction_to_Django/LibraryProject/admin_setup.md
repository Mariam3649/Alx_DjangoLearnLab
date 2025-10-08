# Django Admin Setup for Book Model

## Steps
- Registered the `Book` model in `bookshelf/admin.py`.
- Customized the admin interface using `BookAdmin`:
  - Displayed fields: title, author, publication_year
  - Added list filters for author and publication_year
  - Enabled search by title and author

## Verification
- Created a superuser with `python3 manage.py createsuperuser`
- Logged in at http://127.0.0.1:8000/admin/
- Verified the Book model appears with the custom admin setup

