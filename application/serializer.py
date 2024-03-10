from .models import Application
from rest_framework import serializers 
# from jobs.serializer import JobSerializer
from account.serializer import UserSerializer

class ApplicationSerializer(serializers.ModelSerializer):
    applicant = UserSerializer()
    class Meta:
        model = Application
        fields = '__all__'