from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=(
            'is_customer', 
            'is_cleaner', 
            'username', 
            'last_name', 
            'phone', 
            'email', 
            'is_verified', 
            'avatar', 
            'password'
        )