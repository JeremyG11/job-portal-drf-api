
from django.db import models
from application.models import Application
from account.models import CustomUser as User

# Create your models here.

class CategoryManager(models.Manager):
    def queryset(self, category):
        jobs = Job.objects.filter(category=self.category)
        return jobs


class JobManager(models.Manager):
    def queryset (self):
        return super(JobManager, self).queryset().filter(is_active=True)

  
class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'Catories'


    def __str__(self):
        return self.name



class Job(models.Model):
    category = models.ForeignKey(Category, related_name='jobs', on_delete=models.CASCADE)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Job_poster')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    posted_at = models.DateTimeField(auto_now=True)
    location = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    slug = models.SlugField(max_length=255)
    
        
    objects = models.Manager()
    jobs = JobManager()

    class Meta:
        verbose_name_plural = 'jobs'
        ordering = ('-posted_at',)

    def __str__(self):
        return self.title

    
