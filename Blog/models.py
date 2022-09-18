from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Blog(models.Model):

    '''Model for a blog...'''

    CATEGORY=[
        ('PROGRAMMING', 'Programming'),
        ('TRAVEL', 'Travelling'),
        ('PHOTOGRAPHY', 'Photography'),
    ]

    title=models.CharField(max_length=50)
    content=models.CharField(max_length=100)
    author= models.ForeignKey(User,on_delete=models.CASCADE)
    category= models.CharField(max_length=100,choices=CATEGORY,default='PROGRAMMING')

