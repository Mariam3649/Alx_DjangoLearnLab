from rest_framework import serializers
from .models import Author, Book
import datetime

# BookSerializer: يقوم بتحويل كائن Book ل/من JSON
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'  # serializes all fields: id, title, publication_year, author

    # Validation: نضمن أن سنة النشر ليست في المستقبل
    def validate_publication_year(self, value):
        current_year = datetime.date.today().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value


# AuthorSerializer: يعرض بيانات الـ Author مع الكتب المرتبطة به (nested)
class AuthorSerializer(serializers.ModelSerializer):
    # نستخدم BookSerializer لعرض الكتب المرتبطة كمصفوفة read-only
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        # نُرجع id, name, و قائمة الكتب المرتبطة
        fields = ['id', 'name', 'books']

