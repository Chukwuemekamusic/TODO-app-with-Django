from django.urls import path
from . import views
from .views import UpdateTask

urlpatterns = [
    path("", views.home, name='home'),
    path("login/", views.loginPage, name='login'),
    path("logout/", views.logoutUser, name='logout'),
    path("register/", views.registerUser, name='register-user'),

    path("task/<str:pk>/", views.viewTask, name='task'),
    path("add-task/", views.addTask, name='add-task'),
    path("delete-task/<str:pk>", views.deleteTask, name='delete-task'),
    path("update-task/<str:pk>", UpdateTask.as_view(), name='update-task'),
]
