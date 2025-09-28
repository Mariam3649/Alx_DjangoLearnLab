from django.db import models

# Author model: يمثل مؤلفًا واحدًا
class Author(models.Model):
    # اسم المؤلف
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# Book model: يمثل كتابًا مرتبطًا بمؤلف واحد (One-to-Many)
class Book(models.Model):
    # عنوان الكتاب
    title = models.CharField(max_length=255)
    # سنة نشر الكتاب
    publication_year = models.IntegerField()
    # الربط بالمؤلف: المؤلف يمكن أن يمتلك عدة كتب (related_name="books")
    author = models.ForeignKey(Author, related_name="books", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} ({self.publication_year})"

