from django.urls import path

from . import views

app_name = 'borad'

urlpatterns = [
    path("pepe/", views.pepe, name="pepe"),
    path("index/", views.index, name="index"),
]