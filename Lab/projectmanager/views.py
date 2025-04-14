# projectmanager/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Project, Task
from .forms import ProjectForm, TaskForm


@login_required
def home(request):
    # List projects for the logged-in user
    projects = Project.objects.filter(owner=request.user)
    return render(request, 'projectmanager/home.html', {'projects': projects})


@login_required
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk, owner=request.user)
    tasks = project.tasks.all()
    return render(request, 'projectmanager/project_detail.html', {
        'project': project,
        'tasks': tasks
    })


@login_required
def project_create(request):

    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = request.user  # Set the owner of the project
            project.save()
            return redirect('project_detail', pk=project.pk)
    else:
        form = ProjectForm()
    return render(request, 'projectmanager/project_form.html', {'form': form})


@login_required
def task_create(request, project_id):
    project = get_object_or_404(Project, pk=project_id, owner=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.project = project
            task.save()
            return redirect('project_detail', pk=project.pk)
    else:
        form = TaskForm()
    return render(request, 'projectmanager/task_form.html', {'form': form, 'project': project})


def register(request):
    # User registration using Django's built-in form
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'projectmanager/register.html', {'form': form})
