from django.urls import path
from . import views


urlpatterns = [
    path("", views.index , name="index"),
    path("<int:task>", views.tasks_int),
    path("<str:task>", views.tasks, name="task-name")
    
    
]
