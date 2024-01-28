from django.db import models

# Create your models here.
class userinfo(models.Model):
    UserName=models.CharField(max_length=10)
    userEmail=models.EmailField()
    userPassword=models.IntegerField(max_length=8)
    userConfirmPassword=models.IntegerField(max_length=8)

    def __str__(self):
        return self.UserName
