from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('home/opening_times/', views.opening_times, name='opening_times'),
]   + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
