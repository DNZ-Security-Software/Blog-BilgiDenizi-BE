from typing import Optional
from django.db import models
from django.db.models.fields import BLANK_CHOICE_DASH
from django.contrib.auth.models import User  # import django user model
# Create your models here.

def user_directory_path(instance, filename):
    return 'blog/{0}/{1}'.format(instance.author.id, filename)

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Categories"  # ismi çoğul yaptığında yanlış olanları düzeltme için

class Post(models.Model):
    OPTIONS = (
        ('d', 'Draft'),
        ('p', 'Publised')
    )
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to= user_directory_path, default='dnz-security.png' )
    category = models.ForeignKey(Category, on_delete=models.PROTECT)  # Categoriye ait olan postların kategori silinince silinmesini engellemek için PROTECT
    publish_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # user silinince POST larında silinmesi için CASCADE
    status = models.CharField(max_length=10, choices=OPTIONS, default="d") 
    slug = models.SlugField(blank=True, unique=True)
    
    def __str__(self):
        return self.title