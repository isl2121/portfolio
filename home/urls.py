from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.main, name="main"),
    path('ajax/portfolio/<int:pk>', views.portfolio, name="portfolio")
]
