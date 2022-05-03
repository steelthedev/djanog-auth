
from django.urls import path
from . import views

urlpatterns = [
    path('',views.Login, name="login"),
    path('dashboard',views.Dashboard, name="dashboard")
]
