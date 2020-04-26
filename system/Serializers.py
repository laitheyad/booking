from .models import *
from rest_framework import serializers
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['pk','UserName','Email','Password','PhoneNumber','Acception']

