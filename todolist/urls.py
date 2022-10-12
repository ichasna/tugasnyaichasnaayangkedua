from django.urls import path
from todolist.views import *

app_name = "todolist"

urlpatterns = [
    path('', todolist, name='todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_task, name='create_task'),
    path('delete/<int:id>', delete, name='delete'),
    path('json/', show_json, name='show_json'),
    path('add/', create_task_modal, name='create_task_modal'),
    path('json_ajax/', show_todolist_json, name='show_todolist_json'),  #mengarah ke todolist_ajax.html
]