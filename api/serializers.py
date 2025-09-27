from rest_framework import serializers
from .models import Author, Book
from datetime import datetime

# Serializer للـ Book
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    # validation: سنة النشر ما تبقاش في المستقبل
    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value


# Serializer للـ Author + nested books
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)  # اسم related_name في الموديل Book

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']

