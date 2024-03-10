

from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/jobs/', include('jobs.urls')),
    path('api/application/', include('application.urls')),
    path('api/auth/user/', include('account.api.urls')),
    path('api/auth/users/', include('account.urls')),
    path('api/blogs/', include('blogs.urls')),
    path('api/events/', include('events.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
