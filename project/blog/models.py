from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class post(models.Model):
    title = models.CharField(max_length=50)
    content =models.CharField(max_length=1000)
    author = models.ForeignKey(User , on_delete=models.CASCADE)
    date = models.DateTimeField(default= timezone.now) 
    def __str__(self) :
        return self.title
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk})
    