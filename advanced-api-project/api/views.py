from rest_framework import generics, viewsets
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer
from rest_framework.permissions import AllowAny

# بسيط لعرض قائمة المؤلفين (اختياري)
class AuthorList(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [AllowAny]

# ViewSet للـ Book يدعم CRUD
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]

