from django.urls import path
from . import views

app_name = 'bocej_aguipe'

urlpatterns = [
    path('home', views.home, name='home'),
    path('add_center', views.add_center, name='add_center'),
]