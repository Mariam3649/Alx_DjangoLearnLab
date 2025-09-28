from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .models import Book


class BookAPITests(APITestCase):

    def setUp(self):
        # إنشاء يوزر وتوكن للمصادقة
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

        # إنشاء كتب للتجربة
        self.book1 = Book.objects.create(title="Book One", author="Author A", publication_year=2020)
        self.book2 = Book.objects.create(title="Book Two", author="Author B", publication_year=2021)

    def test_list_books(self):
        url = reverse("book-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 2)

    def test_retrieve_book(self):
        url = reverse("book-detail", args=[self.book1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.book1.title)

    def test_create_book(self):
        url = reverse("book-create")
        data = {"title": "New Book", "author": "Author C", "publication_year": 2022}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(response.data["title"], "New Book")

    def test_update_book(self):
        url = reverse("book-update", args=[self.book1.id])
        data = {"title": "Updated Book", "author": "Author A", "publication_year": 2020}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Book")

    def test_delete_book(self):
        url = reverse("book-delete", args=[self.book2.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_filter_books_by_author(self):
        url = reverse("book-list") + "?author=Author A"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for book in response.data:
            self.assertEqual(book["author"], "Author A")

    def test_search_books_by_title(self):
        url = reverse("book-list") + "?search=Book One"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(any("Book One" in b["title"] for b in response.data))

    def test_order_books_by_year(self):
        url = reverse("book-list") + "?ordering=publication_year"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        years = [book["publication_year"] for book in response.data]
        self.assertEqual(years, sorted(years))

