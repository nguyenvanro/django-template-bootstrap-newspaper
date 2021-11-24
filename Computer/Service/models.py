from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
class CustomUser(AbstractUser):
    Choose_gender = (
        ('Male','Nam'),
        ('Female','Nữ'),
        ('lgbt','Khác'),
    )
    gender = models.CharField(choices=Choose_gender, blank=True, null=True, max_length=20)
    age = models.CharField(max_length=2, blank=True, null=True)
    address = models.CharField(max_length=100,blank=True, null=True )
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    subject = models.CharField(max_length=20)
    message = models.TextField()


class Post(models.Model):
    Status_choices = (
        ('draft','Bản thảo'),
        ('published','Phát hành')
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, )
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    status = models.CharField(max_length=10,choices=Status_choices,default='draft')
    class Meta:
        ordering = ('-publish',)    
    def __str__(self):
        return self.title