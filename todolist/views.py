from re import T
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import datetime
from todolist.models import *
from django.http import HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@login_required(login_url='login/')
def todolist(request):
    tasklist = Task.objects.filter(user=request.user)
    context = {
    'tasks' : tasklist,
    'username' : request.user,
    }
    return render(request, "todolist.html", context)

def create_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')

        if title != "" and description != "":
            Task.objects.create(title=title, description=description, date=datetime.date.today(), user=request.user)
            return HttpResponseRedirect(reverse("todolist:todolist")) 
        
        messages.info(request, 'Judul atau Deskripsi belum diisi!')

    return render(request, "create-task.html")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

def delete(request,id):
    Task.objects.filter(pk=id).delete()
    return HttpResponseRedirect(reverse("todolist:todolist"))

def show_json(request):
    data = Task.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_todolist_json(request):
    tasklist = Task.objects.filter(user=request.user)
    context = {
    'tasks' : tasklist,
    'username' : request.user,
    }
    return render(request, "todolist_ajax.html", context)

@csrf_exempt
def create_task_modal(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        date = datetime.date.today()
        user = request.user
        task = Task.objects.create(title=title, description=description, date=date, user=user)

        result = {
            'fields':{
                'title':task.title,
                'description':task.description,
                'date':task.date,
            },
            'pk':task.pk
        }
        return JsonResponse(result)