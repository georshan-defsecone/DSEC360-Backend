from rest_framework import serializers
from .models import Scan
from .models import User

class ScanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scan
        fields = '__all__'

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [ 'username', 'email','id','is_admin']

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims to token payload
        token['username'] = user.username
        token['email'] = user.email
        token['is_admin'] = user.is_admin

        return token

    def validate(self, attrs):
        data = super().validate(attrs)

        # Include additional user info in the response body
        data['username'] = self.user.username
        data['email'] = self.user.email
        data['is_admin'] = self.user.is_admin

        return data
