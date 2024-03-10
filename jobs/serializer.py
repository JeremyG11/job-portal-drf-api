
from .models import Category, Job
from rest_framework import serializers
from application.serializer import ApplicationSerializer

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name',]
 

class JobSerializer(serializers.ModelSerializer):
    application_set = ApplicationSerializer(many=True, read_only=True)

    class Meta:
        model = Job
        fields = '__all__'
        
        