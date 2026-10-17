from django.urls import path
from AITCSL import views

urlpatterns = [
    path("", views.home),
    path("result", views.result),

]
