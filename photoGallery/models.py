from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models



class Photograph(models.Model):
    
    user = models.ForeignKey(User)

    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    photographer = models.CharField(max_length=100)
    date = models.CharField(max_length=100) # Change to DateField
    image = models.ImageField(upload_to='image_files', default='media/default.png')

    likes = models.IntegerField(default=0)



    def __str__(self):
        return self.name