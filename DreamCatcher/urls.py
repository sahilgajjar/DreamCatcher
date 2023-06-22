from django.urls import path
from . import views

urlpatterns = [
    path("",views.login_view, name="login"),
    path("logout",views.logout_view, name="logout"),
    path("register",views.register, name="register"),
    path("addtask",views.addtask, name="addtask"),
    path("listtask",views.listtask, name="listtask")
]
