from rest_framework import serializers
from .models import Author, Book

# 🔹 Serializer لكتاب (Book)
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    # تحقق من أن سنة النشر مش في المستقبل
    def validate_publication_year(self, value):
        import datetime
        current_year = datetime.date.today().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

# 🔹 Serializer للمؤلف (Author)
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)  # nested relationship

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
