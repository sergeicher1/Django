from django.urls import path, re_path, include
from hello import views

urlpatterns = [
    path('', views.index),
    path("create/", views.create),

]
