from django.urls import path
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPair



class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPair



@api_view (['GET'])
def getRoutes(request):
    routes = [
        'token',  
        'token/refresh', 
    ]
    return Response(routes)