from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.db import models
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

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
    photo = models.ImageField(upload_to='reports/', null=True, blank=True)

    def __str__(self):
        return f'{self.type} Report by {self.author.username} at {self.location}'

    def get_absolute_url(self):
        return reverse('report-detail', kwargs={'pk': self.pk})
    

class Pickup(models.Model):
    address = models.CharField(max_length=255)
    street_name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    time_slot = models.IntegerField(validators=[MinValueValidator(9), MaxValueValidator(18)])  # 24-hour format
    date_of_pickup = models.DateField()
    STATUS_CHOICES = [
        ('pickedup', 'Picked Up'),
        ('pending', 'Pending'),
    ]
    status = models.CharField(max_length=8, choices=STATUS_CHOICES, default='pending')
    TYPE_CHOICES = [
        ('dry', 'Dry'),
        ('wet', 'Wet'),
        ('toxic', 'Toxic'),
    ]
    type = models.CharField(max_length=5, choices=TYPE_CHOICES, default='dry')

    def __str__(self):
        return f'{self.address}, {self.street_name}, {self.city}'