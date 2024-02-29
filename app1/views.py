from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse ,HttpResponseNotFound , HttpResponseRedirect
# Create your views here.

task_dict ={
    "task1":"This is task1",
    "task2":"This is task2",
    "task3":"This is task3",
    "task4":"This is task4",
    "task5":"This is task5",
    "task6":"This is task6",
}

# def task1(request):
#     return HttpResponse("This is task 1")

# def task2(request):
#     return HttpResponse("This is task 2")

def tasks_int(request, task):
    tasks = list(task_dict.keys())
    redirect_task = tasks[task-1]
    return HttpResponseRedirect("/app1/" + redirect_task)

def tasks(request, task):
    try:
        task_text = task_dict[task]
        return HttpResponse(task_text)
    except:
        return HttpResponseNotFound("Invalid Task")
        
# def tasks(request, task):
#     task_text = None
#     if task == "task1":
#         task_text = "This is task1"
#     elif task == "task2":
#         task_text = "This is task2"
#     elif task == "task3":
#         task_text = "This is task3"
#     else:
#         return HttpResponseNotFound("This Task is not availible")
    
#     return HttpResponse(task_text)