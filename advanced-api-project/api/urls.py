from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthorList, BookViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='books')

urlpatterns = [
    path('authors/', AuthorList.as_view(), name='author-list'),
    path('', include(router.urls)),  # يضيف /books/ و /books/<id>/
]
