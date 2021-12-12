from django.shortcuts import render, HttpResponse
from home.models import Task

# Create your views here.
def home(request):
    context = {'success': False, 'name':'Mayur' }
    if request.method == "POST":
        #handle the form
        title = request.POST['title']
        desc = request.POST['desc']
        print(title, desc)
        ins = Task(taskTitle = title, taskDesc = desc )
        ins.save()
        context = {'success': True }

    return render(request, 'index.html', context)

def task(request):
    allTask = Task.objects.all()
    # print(allTask)
    # for item in allTask:
    #     print(item.taskTitle)
    context = {'tasks': allTask}
    return render(request, 'task.html', context)

