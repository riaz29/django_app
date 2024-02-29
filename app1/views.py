from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse ,HttpResponseNotFound
# Create your views here.

# def task1(request):
#     return HttpResponse("This is task 1")

# def task2(request):
#     return HttpResponse("This is task 2")

def tasks(request, task):
    task_text = None
    if task == "task1":
        task_text = "This is task1"
    elif task == "task2":
        task_text = "This is task2"
    elif task == "task3":
        task_text = "This is task3"
    else:
        return HttpResponseNotFound("This Task is not availible")
    
    return HttpResponse(task_text)