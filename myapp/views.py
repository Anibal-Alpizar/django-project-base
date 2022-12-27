from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from .form import CreateNewTask
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
    #projects = list(Project.objects.values())
    projects  = Project.objects.all()
    return render(request, 'projects.html', {
        'projects' : projects
    })
    #return JsonResponse(projects, safe=False)

def tasks(request):
    #task = Task.objects.get(id=id)
    #task = get_object_or_404(Task, id=id)
    task = Task.objects.all()
    return render(request, 'tasks.html',{
        'task' : task
    })
    #return HttpResponse('task: %s' % task.title)

def create_task(request):
   
   if request.method == 'GET':
        # SHOW INTERFACE  
            return render(request, 'create_task.html',{
        'form' : CreateNewTask()
    })
   else:
        Task.objects.create(
        title=request.POST['title'], 
        description=request.POST['description'], 
        project_id=1
        )
        return redirect('/tasks/')




