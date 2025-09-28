from rest_framework.test import APITestCase
from rest_framework import status
from .models import Author, Book
from django.contrib.auth.models import User

class BookAPITestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.author = Author.objects.create(name='Author 1')
        self.book = Book.objects.create(title='Book 1', publication_year=2020, author=self.author)
        self.client.login(username='testuser', password='12345')

    def test_create_book(self):
        data = {'title': 'Book 2', 'publication_year': 2021, 'author': self.author.id}
        response = self.client.post('/api/books/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # استخدام response.data للتحقق من المحتوى
        self.assertEqual(response.data['title'], 'Book 2')
        self.assertEqual(response.data['publication_year'], 2021)

    def test_list_books(self):
        response = self.client.get('/api/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # التحقق من البيانات مباشرة
        self.assertEqual(response.data[0]['title'], 'Book 1')

    def test_update_book(self):
        data = {'title': 'Book 1 Updated', 'publication_year': 2022, 'author': self.author.id}
        response = self.client.put(f'/api/books/{self.book.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, response.data['title'])
        self.assertEqual(self.book.publication_year, response.data['publication_year'])

    def test_delete_book(self):
        response = self.client.delete(f'/api/books/{self.book.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book.id).exists())

