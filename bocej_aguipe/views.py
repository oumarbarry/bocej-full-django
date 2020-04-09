from django.shortcuts import render
from login.models import UserBA
from center.models import Center
from bocej_aguipe.forms import *
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    user_profile = UserBA.objects.get(user=request.user)
    return render(request, 'bocej_aguipe/home.html', locals())

@login_required
def add_center(request):
    if request.method == 'POST':
        center_form = CenterForm(data=request.POST)
        if center_form.is_valid:
            center_form.save()

        username = request.POST['username']
        
        #user_center_form = UserCenter(user=user)
    else:
        center_form = CenterForm()
        user_center_form = UserCenterForm()

    return render(request, 'bocej_aguipe/add_center.html', locals())