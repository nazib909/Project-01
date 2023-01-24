from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class userProfile(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=10,null=True,blank=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES,null=True,blank=True)
    phone = models.TextField(max_length=11,null=True,blank=True)
    address = models.TextField(max_length=30,null=True)
    birthday = models.DateField(auto_now=False, null=True, blank=True)
    image = models.ImageField(upload_to ='user/',null=True,blank=True)

    def __str__(self):
        return self.user.username