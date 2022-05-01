from django import views
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.apiOverview, name="apiOverview"),
    path('ctlist/', views.categorylist, name="categorylist"),
    path('ctdetails/<str:pk>/', views.categoryDetails, name="categoryDetails"),
    path('leclist/', views.lecturelist, name="lecturelist"),
    path('lecdetails/<str:pk>/', views.lectureDetails, name="lectureDetails"),

]
