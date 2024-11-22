from django.db import models

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=20)
    author=models.CharField(max_length=20)
    pages=models.IntegerField()
    price=models.IntegerField()
    language=models.CharField(max_length=20)
    image=models.ImageField(upload_to="images")
    y=models.FileField(upload_to="pdf")
    def __str__(self):
        return self.title
