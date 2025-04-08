from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('projects/', views.projects, name='projects'),
    path('projects/create_project/', views.create_project, name='create_project'),
    path('projects/edit_project/', views.edit_project, name='edit_project'),
    path('bugs/', views.bugs, name='bugs'),
    path('bugs/create_bug/', views.create_bug, name='create_bug'),
    path('bugs/edit_bug/', views.edit_bug, name='edit_bug'),
]