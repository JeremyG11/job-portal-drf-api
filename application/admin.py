from email.mime import application
from django.contrib import admin
from .models import Application
# Register your models here.


@admin.register(Application)
class ApplicantionModelAdmin(admin.ModelAdmin):
    list_display = ['applicant', 'job']
