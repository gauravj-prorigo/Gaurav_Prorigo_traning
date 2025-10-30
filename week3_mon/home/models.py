from django.db import models
from django.contrib.auth.models import AbstractUser
# class Students(models.Model):
#     name = models.CharField(max_length=100)
#     age = models.IntegerField()
#     email = models.EmailField(unique=True)
#     address = models.TextField(null=True, blank=True)
#     image = models.ImageField(upload_to='students/', null=True, blank=True)

#     def __str__(self):
#         return self.name


class Blog(models.Model):
    title = models.CharField(max_length=200, default="Untitled")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
     return f"{self.title} - {self.content[:30]}" 


class person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    
    
    
class loginuser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('employee', 'Employee'),
        ('user', 'User'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')

    def __str__(self):
        return f"{self.username} ({self.role})"    