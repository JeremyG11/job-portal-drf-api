from django.urls import path
from .views import application_list_create, application_update_delete

urlpatterns = [
    path('', application_list_create, name='applications'),
    path('<int:pk>/', application_update_delete, name='application_update')
]
