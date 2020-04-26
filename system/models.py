from django.db import models

class User(models.Model):
    UserName=models.CharField(max_length=500)
    Email=models.EmailField(null=True)
    Password=models.CharField(max_length=500)
    PhoneNumber=models.IntegerField(max_length=10)
    acception_status=[
        ('YES','YES'),
        ('NO','NO')
    ]
    Acception=models.CharField(max_length=3,choices=acception_status,default='YES')
    def __str__(self):
        return  self.username