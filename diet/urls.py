from . import views

from django.urls import path

app_name = "diet"

urlpatterns = [
    path("index", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("sum/", views.sum, name="sum"),
    path("create/", views.create, name="create"),
]
