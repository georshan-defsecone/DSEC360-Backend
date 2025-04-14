from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view,permission_classes
from rest_framework import status
from rest_framework.response import Response
from .models import Scan, Project
from .serializers import ScanSerializer, ProjectSerializer
from rest_framework.permissions import AllowAny


#get projects
@api_view(['GET'])
@permission_classes([AllowAny])
def get_projects_view(request):
    projects = Project.objects.filter(trash=False)
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)

#create project only in djangorestframework
@api_view(['POST'])
@permission_classes([AllowAny])
def create_project_view(request):
    serializer = ProjectSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#trash project
@api_view(['PUT'])
@permission_classes([AllowAny])
def update_project_view(request, project_id):
    try:
        project = Project.objects.get(project_id=project_id)
    except Project.DoesNotExist:
        return Response({'error': 'Project not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = ProjectSerializer(project, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#trashed projects
@api_view(['GET'])
@permission_classes([AllowAny])
def trashed_projects_view(request):
    trashed_projects = Project.objects.filter(trash=True)
    serializer = ProjectSerializer(trashed_projects, many=True)
    return Response(serializer.data)


#get scans
@api_view(['GET'])
@permission_classes([AllowAny])
def get_scans_view(request):
    scans = Scan.objects.filter(trash=False)
    serializer = ScanSerializer(scans, many=True)
    return Response(serializer.data)

#create scan only in djangorestframework
@api_view(['POST'])
@permission_classes([AllowAny])
def create_scan_view(request):
    serializer = ScanSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#trash scan
@api_view(['PUT'])
@permission_classes([AllowAny])
def update_scan_view(request, pk):
    try:
        scan = Scan.objects.get(pk=pk)
    except Scan.DoesNotExist:
        return Response({'error': 'Scan not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = ScanSerializer(scan, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#get scans by project id
@api_view(['GET'])
@permission_classes([AllowAny])
def get_project_scans_view(request, project_id):
    scans = Scan.objects.filter(project_id=project_id, trash=False)
    serializer = ScanSerializer(scans, many=True)
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

# @api_view(['GET'])
# @permission_classes([IsAdminUserCustom])
# def project_scans_view(request, project_id):
#     print("scans")
#     try:
#         scans = Scan.objects.filter(project_id=project_id, trash=False)
        
#         serializer = ScanSerializer(scans, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     except Scan.DoesNotExist:
#         return Response({"error": "No scans found for this project"}, status=status.HTTP_404_NOT_FOUND)
