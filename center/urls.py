from django.urls import path
from . import views

app_name = 'center'

urlpatterns = [
    path('home', views.home, name='home'),
]