from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path("", main, name="home"),
    path("news/", news, name="news"),
    path("new/<int:new_pk>", new),
    path("terminal/<int:terminal_pk>/", terminal),
    path("service/<int:service_pk>/", service),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
