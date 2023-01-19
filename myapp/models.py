from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField()

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

class Contact(models.Model):
    name=models.CharField(max_length=70)
    phone=models.IntegerField()
    email=models.EmailField(max_length=100)
    message=models.TextField(max_length=1000)
