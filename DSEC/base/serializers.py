from rest_framework import serializers
from .models import User  # Assuming your custom user model is named User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [ 'username', 'email']