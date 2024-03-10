from django.db import models
from jobs.models import Category
from account.models import CustomUser as User
# Create your models here.


class BlogManager(models.Manager):
    def queryset(self):
        return super(BlogManager, self).queryset()


class Blog(models.Model):
    category = models.ForeignKey(
        Category, related_name='jobs_post', on_delete=models.CASCADE)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_poster')
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='Images/blogs/images/', default='user/post1/default.png')
    posted_at = models.DateTimeField(auto_now=True)
    location = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)

    objects = models.Manager()
    jobs = BlogManager()

    class Meta:
        verbose_name_plural = 'blogs'

    def __str__(self):
        return self.title
