from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class post(models.Model):
    title = models.CharField(max_length=50)
    content =models.CharField(max_length=700)
    author = models.ForeignKey(User , on_delete=models.CASCADE)
    date = models.DateTimeField(default= timezone.now)
  
    def __str__(self) :
        return self.title
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk})

class report(models.Model):
    location = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    STATUS_CHOICES = (
        ('Open', 'Open'),
        ('Closed', 'Closed'),
    )
    status = models.CharField(max_length=6, choices=STATUS_CHOICES, default='Open')

    def __str__(self):
        return f'{self.type} Report by {self.author.username} at {self.location}'

    def get_absolute_url(self):
        return reverse('report-detail', kwargs={'pk': self.pk})  