from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view,permission_classes
from rest_framework import status
from rest_framework.response import Response
from .models import Scan
from .serializers import ScanSerializer
from rest_framework.permissions import AllowAny

@api_view(['GET'])
@permission_classes([AllowAny])
def my_projects_view(request):
    project = Scan.objects.filter(trash=False)
    serializer = ScanSerializer(project, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([AllowAny])
def add_MyProjectsView(request):
    serializer = ScanSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([AllowAny])
def update_MyProjectsView(request, project_id):
    try:
        project = Scan.objects.get(pk=project_id)
        project.trash = True
        project.save()
        return Response({"message": "project moved to trash"}, status=status.HTTP_200_OK)
    except Scan.DoesNotExist:
        return Response({"error": "project not found"}, status=status.HTTP_404_NOT_FOUND)
    

@api_view(['GET'])
@permission_classes([AllowAny])
def trashed_project_view(request):
    trashed_project = Scan.objects.filter(trash=True)
    serializer = ScanSerializer(trashed_project, many=True)
    return Response(serializer.data)

# Create your views here.
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import MyTokenObtainPairSerializer

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer
from .permissions import IsAdminUserCustom

@api_view(['GET'])
@permission_classes([IsAdminUserCustom])
def get_all_users(request):
    users = User.objects.all()  
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)
