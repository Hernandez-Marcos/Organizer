from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import TaskForm

# Create your views here.

#@login_required
def index(request):
    return render(request, "tasks/index.html")


@login_required
def createTask(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('tasks:index')
    else:
        form = TaskForm()
        
    return render(request, 'tasks/form.html', {"form": form})
 