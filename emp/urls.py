from django.contrib import admin
from django.urls import path, re_path, include
from emp import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    #re_path(r'^$', views.home, name='home'),
    re_path(r'^emp', views.emp, name='emp'),
    re_path(r'^leave', views.leave, name='leave'),
    re_path(r'^holiday', views.holiday, name='holiday'),



]
