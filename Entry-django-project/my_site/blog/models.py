from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.
class Tag(models.Model):
    caption = models.CharField(max_length=30)

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.CharField(max_length=50, null=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()




class Post(models.Model):

    title = models.CharField(max_length=30)
    excerpt = models.CharField(max_length=50)
    image_name = models.ImageField(upload_to='blog/images')
    date = models.DateField()
    slug = models.SlugField(default="", blank=True, null=False, db_index=True)
    content = models.CharField(max_length=300)
    tag = models.ManyToManyField(Tag)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
