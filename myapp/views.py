from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from .form import CreateNewTask, CreateNewProject
from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    title = 'Django Course!!'
    return render(request , 'index.html', {
        'title' : title
    })

def about(request):
    username = 'anibal'
    return render(request,'about.html', {
        'username' : username
    })

def hello(request, username):
    return HttpResponse("<h3>Hello %s</h3>" % username)

def projects(request):
    projects  = Project.objects.all()
    return render(request, 'projects/projects.html', {
        'projects' : projects
    })

def tasks(request):
    task = Task.objects.all()
    return render(request, 'tasks/tasks.html',{
        'task' : task
    })

def create_task(request):
   if request.method == 'GET':
        # SHOW INTERFACE  
            return render(request, 'tasks/create_task.html',{
        'form' : CreateNewTask()
    })
   else:
        Task.objects.create(
        title=request.POST['title'], 
        description=request.POST['description'], 
        project_id=1
        )
        return redirect('tasks')

def create_project(request):
    if request.method == 'GET':
        return render(request, 'projects/create_project.html', {
            'form' : CreateNewProject()
        })
    else: 
        Project.objects.create(name = request.POST['name']
        )
        redirect('projects')
       
        