from django.db import models
from django.conf import settings

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, 
                                on_delete=models.CASCADE)
    
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d',
                                blank=True)
    sex = models.CharField(max_length=50, blank=True)
    country = models.CharField(blank=True, max_length=100)
    state = models.CharField(blank=True, max_length=1000)
    education_level = models.CharField(blank=True, max_length=255)
    description = models.TextField(blank=True)
    mobile_1 = models.IntegerField(blank=True, null=True)
    mobile_2 = models.IntegerField(blank=True, null=True)
    
    def __str__(self):
        return f'Profile for user {self.user.username}'