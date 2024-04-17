from django.contrib.auth.models import AbstractUser # type: ignore
from django.db import models # type: ignore
from rest_framework_simplejwt.tokens import RefreshToken # type: ignore
from django.conf import settings # type: ignore

class User(AbstractUser):
    email = models.EmailField(unique=True, max_length=50)
      
    USERNAME_FIELD = ['first_name', 'last_name', 'username']
    REQUIRED_FIELDS ='email' # add phone number as a requirement while signing up     
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
    def __str__(self):
        return "{}".format(self.email)     
    def tokens(self):
        refresh= RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }
    
# Create your models here.
class Item(models.Model):
    Question = models.CharField(max_length=255, default="what is the rent roll of ...")
    Created = models.DateTimeField(auto_now_add=True)
    Created_By =  models.CharField(max_length=255)
    Title = models.CharField(max_length=255)
    Department = models.CharField(max_length=255, default="orient")
 
    # def __str__(self) -> str:
    #     return self.name
    
   
    def __str__(self):
        return self.title
    