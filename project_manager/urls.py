"""project_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings #new
from django.conf.urls.static import static #new
from app1 import views


urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),    
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('service/', views.service, name='service'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('ws/', views.ws, name='ws'),
    path('ws2/', views.ws2, name='ws2'),
    path('ws3/', views.ws3, name='ws3'),
    path('createws/', views.createws, name='createws'),
    path('createws2/', views.createws2, name='createws2'),
    path('createws3/', views.createws3, name='createws3'),
    path('library/', views.library, name='library'),
    path('logout/', views.LogoutPage, name='logout'),  


]


if settings.DEBUG:
    urlpatterns += static( settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)