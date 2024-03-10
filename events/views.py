from django.shortcuts import render
from .models import Events
from rest_framework import generics
from .serializer import EventSerializer
# Create your views here.


class EventListView(generics.ListCreateAPIView):
    queryset = Events.object.all()
    serializer_class = EventSerializer
