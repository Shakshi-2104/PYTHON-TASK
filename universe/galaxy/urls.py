from django.urls import path
from . import views

urlpatterns = [
    path('galaxy/', views.galaxy, name='galaxy'),
    path('', views.homepage, name='mypage'),
    path('home', views.home, name='mypage'),
    path('aboutus', views.aboutus, name='mypage'),
    path('service', views.service, name='mypage'),
    path('contact', views.contact, name='mypage'),
    path('dynamic', views.dynamic, name='mypage'),
]
