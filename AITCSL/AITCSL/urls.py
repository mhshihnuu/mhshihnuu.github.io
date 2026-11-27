from django.urls import path
from AITCSL import views

urlpatterns = [
    path("index", views.index),
    path("", views.home),
    path("result", views.result),

]
