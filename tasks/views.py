from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import TaskForm
from .models import Task
from django.contrib import messages

# Create your views here.

@login_required
def index(request):
    tasks = Task.objects.filter(user=request.user).order_by("-id")
    context = {"tasks": tasks}
    return render(request, "tasks/index.html", context)

@login_required
def task(request, pk):
    task = get_object_or_404(Task, id=pk, user=request.user)

    return render(request, "tasks/task.html", {"task": task})

@login_required
def createTask(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            messages.success(request, "Task created successfully")
            return redirect("tasks:index")
        else:
            messages.error(request, "Please correct the errors below")
    else:
        form = TaskForm()

    return render(request, "tasks/form.html", {"form": form})


@login_required
def updateTask(request, pk):
    task = get_object_or_404(Task, id=pk, user=request.user)

    if request.method =="POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, "Task updated successfully")
            return redirect("tasks:index")
        else:
            messages.error(request, "Please correct the errors below")
    else:
        form = TaskForm(instance=task)
    return render(request, "tasks/form.html", {"form": form})


@login_required
def deleteTask(request, pk):
    task = get_object_or_404(Task, id=pk, user=request.user)

    if request.method == "POST":
        task.delete()
        messages.success(request, "Task deleted succesfully")
        return redirect("tasks:index")

    return render(request, "tasks/delete-task.html", {"task": task})

    