from django.contrib import admin
from .models import Events

# Register your models here.


@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'address']
