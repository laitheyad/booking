from django.db import models

class User(models.Model):
    username=models.CharField(max_length=500)
    email=models.EmailField(null=True)
    password=models.CharField(max_length=500)
    phone=models.IntegerField(max_length=10)
    acception_status=[
        ('YES','YES'),
        ('NO','NO')
    ]
    acception=models.CharField(max_length=3,choices=acception_status,default='YES')
    def __str__(self):
        return  self.username