from django.urls import path
from reg import views

urlpatterns = [

    path(r'registration/', views.authregistration, name='registration'),
    path(r'login', views.authlogin, name='login'),
    path(r'logout/', views.authlogout, name='logout'),

]
