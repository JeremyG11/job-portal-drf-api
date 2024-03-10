
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .models import Job, Category
from .permissions import JobPermission
from .serializer import JobSerializer, CategorySerializer 
from django.core.mail import send_mail

# Create your views here.

class CategoryLiewView(generics.ListCreateAPIView):
    queryset = Category.objects.all() 
    serializer_class = CategorySerializer


class JobListView(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer



@api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes([JobPermission])
def job_detail(request, pk):

    try:
        job = Job.objects.get(pk=pk)
    except Job.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = JobSerializer(job)
        return Response(serializer.data)


    elif request.method == 'PUT':
        serializer = JobSerializer(job, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
            
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    
    elif request.method == 'DELETE':
        job.delete()
        return Response(status=status.HTTP_204_NOT_CONTENT)


@api_view(['GET'])
def job_applications(request, pk):
    try:
        job = Job.objects.get(pk=pk)
    except Job.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        application = JobSerializer(job)
        applications = application.data['application_set']
        return Response(applications)
        send_mail('subject', 'message', 'barodev3211@gmail.com',['gatwech3211@gmail.com'])

 