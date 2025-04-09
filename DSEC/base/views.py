from django.shortcuts import render

# Create your views here.
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import MyTokenObtainPairSerializer

#used for authertication of jwt and to send the data to backend
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth.models import User  # Replace with your custom user model if needed

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_user(request):
    jwt_authenticator = JWTAuthentication()

    # Extract token from Authorization header
    auth_header = request.headers.get('Authorization')
    if not auth_header:
        return Response({'detail': 'Authorization header missing'}, status=status.HTTP_401_UNAUTHORIZED)

    try:
        token = auth_header.split(' ')[1]
        validated_token = jwt_authenticator.get_validated_token(token)
        payload = validated_token.payload
    except Exception:
        return Response({'detail': 'Invalid token'}, status=status.HTTP_401_UNAUTHORIZED)

    # Only admins can insert new users
    if not payload.get('is_admin', False):
        return Response({'detail': 'Access denied. Admins only.'}, status=status.HTTP_403_FORBIDDEN)

    # Extract all fields from the request
    name = request.data.get('name')
    email = request.data.get('email')
    password = request.data.get('password')
    role = request.data.get('role')  # admin / standard

    # Check if all required fields are present
    if not all([name, email, password, role]):
        return Response({'detail': 'Name, email, password, and role are required.'}, status=status.HTTP_400_BAD_REQUEST)

    # Determine is_admin based on role
    is_admin = True if role.lower() == 'admin' else False

    # Create user (replace with custom model if needed)
    user = User.objects.create_user(username=name, email=email, password=password)

    # If you're using a custom User model with is_admin field, set it like this:
    user.is_staff = is_admin  # or user.is_admin = is_admin for custom field
    user.save()

    return Response({"message": f"User '{name}' with role '{role}' created successfully."}, status=status.HTTP_201_CREATED)
