from django.urls import path
from . import views

urlpatterns = [
    path("",views.login_view, name="login"),
    path("logout",views.logout_view, name="logout"),
    path("register",views.register, name="register"),
    path("addtask",views.addtask, name="addtask"),
    path("listtask",views.listtask, name="listtask"),
    path("deletetask/<int:task_id>/", views.deltask, name="delete"),
    path("markasdone/<int:task_id>/",views.markasdone_task, name="markasdone"),
    path("markasdone_add/<int:task_id>/",views.markasdone_add, name="markasdone_add"),
    path("notes",views.notes, name="notes")
]
