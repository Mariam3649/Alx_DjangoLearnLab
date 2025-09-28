from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

# 🔹 List all books OR create a new one
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # السماح للكل بالقراءة لكن الإنشاء محتاج تسجيل دخول
    def get_permissions(self):
        if self.request.method == "POST":
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

# 🔹 Retrieve, Update, or Delete a single Book
class BookRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # السماح للكل بالقراءة لكن التعديل/الحذف محتاج تسجيل دخول
    def get_permissions(self):
        if self.request.method in ["PUT", "PATCH", "DELETE"]:
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

