from django.shortcuts import render
from django.urls import reverse
from login.models import *
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse

def login(request):
    try_login = False
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            try:
                user_ba = UserBA.objects.get(user=user)
            except UserBA.DoesNotExist:
                user_center = UserCenter.objects.get(user=user)
                if user_center.type == 'center' and user_center.role == 'admin':
                    return HttpResponseRedirect(reverse('center:home'))  
            else:
                if (user_ba.type == 'bocej' or user_ba.type == 'aguipe') and user_ba.role == 'admin':
                    return HttpResponseRedirect(reverse('bocej_aguipe:home'))
        else:
            try_login = True
    
    return render(request, 'login/login.html', locals())

@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('login:login'))