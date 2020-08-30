from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='bogiblog-home'),
    path('contact/', views.contact, name='bogiblog-contact'),
    path('login/', views.loginpage, name='bogiblog-login'),
    path('logout/', views.logoutUser, name='bogiblog-logout'),
]