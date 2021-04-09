"""Url patterns for Filmovie"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from movies.views import redirect_to_home


urlpatterns = [
    path('', redirect_to_home, name='home-page'),
    path('admin/', admin.site.urls),
    path('movie/', include('movies.urls')),
    path('actors/', include('actors.urls')),
    path('accounts/', include('users.urls')),
    path('users/', include('users.urls2')),
    path('notifications/', include('notifications.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)