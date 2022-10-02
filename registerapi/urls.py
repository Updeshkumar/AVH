from django.urls import path
from registerapi import views

urlpatterns = [
    path('register/', views.ProfileView.as_view(), name="register"),
    path('list/', views.ProfileView.as_view(), name="list" ),

]