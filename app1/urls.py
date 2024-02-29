from django.urls import path
from . import views


urlpatterns = [
    # path("task1", views.task1),
    # path("task2", views.task2)
    path("<task>", views.tasks)
]
