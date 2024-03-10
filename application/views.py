from rest_framework import status
from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from .models import Application
from .permissions import isApplicationOwner
from .serializer import ApplicationSerializer
# Create your views here.


@api_view(['GET', 'POST'])
@permission_classes([isApplicationOwner])
def application_list_create(request):
    """
        Get a user application and applying for a job
    """
    if request.method == 'GET':
        application = Application.objects.filter(applicant=request.user)
        serializer = ApplicationSerializer(application, many=True)
        print(request.user.id, application)
        return Response(serializer.data, status=status.HTTP_200_OK)
        

    elif request.method == 'POST':
        application = Application.objects.create(data=request.data)
        if application.is_valid():
            application.save()
            return Response(application.data, status=status.HTTP_201_CREATED)
        return  Response(application.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['PUT','DELETE', 'PATCH'])
@permission_classes([isApplicationOwner])
def application_update_delete(request, pk):
    try:
        application = Application.objects.get(pk=pk)
    except Application.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        updated_application = ApplicationSerializer(application, data=request.data)
        if updated_application.is_valid():
            updated_application.save()
            return Response(updated_application.data, status,status.HTTP_200_OK)

        return Response(updated_application.errors, status=status.HTTP_404_NO_CONTENT)
    
    elif request.method == 'DELETE':
        application.delete()
        message = 'Application deleted successfully'
        return Response(message, status=status.HTTP_200_OK)

 