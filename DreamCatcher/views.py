from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Task, User 
from datetime import datetime
from django.shortcuts import redirect
from django.contrib import messages
# Create your views here.

@login_required
def markasdone_add(request, task_id):
    
    tasks = Task.objects.get(id=task_id)
    tasks.complete = True; 
    tasks.save()    
    
    messages.success(request, 'Task Completed Successfully 🎊')
    
    return redirect('addtask')


@login_required
def markasdone_task(request, task_id):
    
    tasks = Task.objects.get(id=task_id)
    tasks.complete = True; 
    tasks.save()    
    
    messages.success(request, 'Task Completed Successfully 🎊')
    
    return redirect('listtask')

@login_required
def deltask(request, task_id):
    
    tasks = Task.objects.get(id=task_id)
    tasks.delete()
     
    messages.success(request, 'Task Deleated Successfully 🗑️')
    
    return redirect('listtask')

@login_required
def listtask(request):
    tasks = Task.objects.filter(complete=False)

    return render(request, "DreamCatcher/listtask.html", {
        "tasks": tasks
    })

@login_required
def addtask(request):
    
    tasks = Task.objects.filter(complete=False).order_by('-id')[:4]
    
    if request.method == "POST":
        
        content = request.POST 
        name = content["name"]
        description = content["description"] 
        date_time = content["time"] 
        label = content["label"]
        time = datetime.strptime(date_time, "%Y-%m-%dT%H:%M")
        
        task = Task.objects.create(
            user=request.user,
            name=name,
            description=description,
            datetime=time,
            label=label
        ) 
        
        messages.success(request, ' Task Added Successfully 🎯')
        
        return redirect("addtask");
        
    return render(request, "DreamCatcher/addtask.html", {
        "tasks": tasks
    })

def login_view(request):
    if request.method == "POST":

        #Attempt to sign user in 
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("addtask"))
        else:
            print("login unsuccessful")
            return render(request, "DreamCatcher/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "DreamCatcher/login.html")

def logout_view(request):
    logout(request) 
    return HttpResponseRedirect(reverse("login"))

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]

        if password != confirmation:
            return render(request, "DreamCatcher/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "DreamCatcher/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "DreamCatcher/register.html")

