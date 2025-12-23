from django.urls import path
from . import views

app_name = "tasks"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:pk>/", views.task, name="task"),
    path("create-task/", views.createTask, name="create-task"),
    path("update-task/<int:pk>/", views.updateTask, name="update-task"),
    path("delete-task/<int:pk>/", views.deleteTask, name="delete-task"),
]