from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("trending/", views.trending, name="trending"),
    path("upload/", views.upload, name="upload"),
    path("categories/", views.categories, name="categories")
]