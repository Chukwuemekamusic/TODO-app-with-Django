from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("login/", views.loginPage, name='login'),
    path("logout/", views.logoutUser, name='logout'),
    path("register/", views.registerUser, name='register-user'),

    path("task/<str:pk>/", views.viewTask, name='task'),
    path("add/", views.addTask, name='add-task'),
    path("delete/<str:pk>", views.deleteTask, name='delete'),
]
