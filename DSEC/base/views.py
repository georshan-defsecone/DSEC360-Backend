from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view,permission_classes
from rest_framework import status
from rest_framework.response import Response
from .models import Scan
from .serializers import ScanSerializer
#from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny

class MyProjectsView(APIView):
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]
    
    def get(self, request):
        scans = Scan.objects.filter(trash=False)
        serializer = ScanSerializer(scans, many=True)
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
def update_MyProjectsView(request, scan_id):
    try:
        scan = Scan.objects.get(scan_id=scan_id)
        scan.trash = True
        scan.save()
        return Response({"message": "Scan moved to trash"}, status=status.HTTP_200_OK)
    except Scan.DoesNotExist:
        return Response({"error": "Scan not found"}, status=status.HTTP_404_NOT_FOUND)