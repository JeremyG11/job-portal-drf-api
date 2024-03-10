from django.contrib import admin
from .models import Job, Category
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name',]


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'description','posted_by'
                    ,'posted_at','is_active','location' ] 
