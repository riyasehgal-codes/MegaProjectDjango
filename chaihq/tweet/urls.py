from . import views
from django.contrib import admin
from django.templatetags import static
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
]
