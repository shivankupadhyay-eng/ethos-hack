from django.db import models

class people(models.Model):
    first_name=models.CharField(max_length=100,null=False)
    last_name=models.CharField(max_length=100,null=False)
    username=models.CharField(max_length=100,null=False,default='default_username')
    email=models.EmailField(null=False)
    password1=models.CharField(max_length=100)
    password2=models.CharField(max_length=100)
    def __str__(self):
        return self.first_name