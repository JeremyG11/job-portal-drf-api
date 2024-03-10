
from django.urls import path
from .views import job_applications
from .views import JobListView, CategoryLiewView, job_detail

urlpatterns = [
    path('categories/', CategoryLiewView.as_view(), name='categories'),
    path('', JobListView.as_view(), name='job'),
    path('<int:pk>/', job_detail, name='update_job'),
    path('applications/job/<int:pk>', job_applications, name='job_applications')

]
