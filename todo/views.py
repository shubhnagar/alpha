from django.shortcuts import render,redirect
from . models import Todo
from django.utils import timezone
from django.contrib.auth.decorators import login_required 

# Create your views here.
def home(request):
    return render(request,'todo/home.html')

@login_required
def create(request):
        if request.method == 'POST': 
            if request.POST['task'] and request.POST['complete_by'] and request.POST['started_on'] and request.POST['description']: 
                todo = Todo() 
                todo.task = request.POST['task']   
                todo.complete_by = request.POST['complete_by']
                todo.started_on = request.POST['started_on']
                todo.description = request.POST['description'] 
                todo.hunter = request.user 
                todo.save() 
                return redirect('home')           
            else: 
                return render(request, 'todo/create.html',{'error':'All field required'})   
        else: 
            return render(request, 'todo/create.html') 
    

