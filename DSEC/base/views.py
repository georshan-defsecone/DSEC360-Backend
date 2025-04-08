from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Scan
from .serializers import ScanSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny

class MyProjectsView(APIView):
    permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]
    
    def get(self, request):
        scans = Scan.objects.filter(trash=False)
        serializer = ScanSerializer(scans, many=True)
        return Response(serializer.data)
