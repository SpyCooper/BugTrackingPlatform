from django.urls import path
from . import views

# URL patterns for the bugs app

urlpatterns = [
    path('', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('projects/', views.projects, name='projects'),
    path('projects/create_project/', views.create_project, name='create_project'),
    path('projects/edit_project/<int:project_id>/', views.edit_project, name='edit_project'),
    path('projects/<int:project_id>/bugs/', views.bugs, name='bugs'),
    path('projects/<int:project_id>/bugs/create_bug/', views.create_bug, name='create_bug'),
    path('projects/<int:project_id>/bugs/edit_bug/<int:bug_id>/', views.edit_bug, name='edit_bug'),
]