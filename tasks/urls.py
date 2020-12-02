from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tasks', views.getTasks, name='tasks'),
    path('tasks/create', views.createTask, name='create'),
]
