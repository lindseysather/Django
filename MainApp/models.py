from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    #string method to show text of topic 
    def __str__(self):
        #doesn't just show weird object - shows text of object
        return self.text

class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        #returns first 50 characters of text
        return f"{self.text[:50]}..."

'''KNOW THIS!!!!!!'''
#To change database:
    #python manage.py makemigrations
    #python manage.py migrate
#To make it seen on admin portal:
    #admin.py