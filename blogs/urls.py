from .views import BlogListView
from django.urls import path

urlpatterns = [
    path('', BlogListView.as_view(), name='blogs'),

]
