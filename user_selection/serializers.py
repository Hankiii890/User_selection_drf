from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        models = User
        fields = ['id', 'email', 'role', 'offer', 'avatar']