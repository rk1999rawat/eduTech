from django.db import models

# Create your models here.
class Contact(models.Model):
    author=models.CharField(max_length=122)
    email=models.EmailField(max_length=126)
    subject=models.CharField(max_length=160)
    comment=models.TextField(max_length=190)

def __str__(self):
    return self.name    




     
