from django.urls import path
from . import views


urlpatterns = [
    # path("task1", views.task1),
    # path("task2", views.task2)
    path("<int:task>", views.tasks_int),
    path("<str:task>", views.tasks)
    
]
