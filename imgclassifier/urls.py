from django.contrib import admin
from django.urls import path, include
from . import views
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('classifier', classifyView.as_view(), name='homepage'),
    path('api/imgclass', uploadView.as_view(),name='Image Classifier'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
