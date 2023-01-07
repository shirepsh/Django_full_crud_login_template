from django.contrib import admin
from django.urls import path
from app import views
from . import views

urlpatterns = [
    path('teacher/<int:_id>', views.teacher),
    path('teacher/', views.teacher),
    path('login/', views.MyTokenObtainPairView.as_view()),
]
