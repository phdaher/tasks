from django.urls import path

from . import views

urlpatterns = [
    path('', views.getTasks, name='tasks'),
    path('create', views.createTask, name='create'),
    path('hello', views.hello, name='hello'),
]
