from django.shortcuts import render, redirect
from django.contrib import messages
from conversations.forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

User = get_user_model()

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account successfully created!')
            return redirect('login')
        context = {
            "page":"register",
            "form" : form
        }
    else:
        context = {
            "page":"register",
            "form" : UserRegistrationForm()
        }
    return render(request,"auth/register.html",context)

@login_required
def profile(request):
    user = User.objects.get(id=request.user.id)
    params = {
        'user': user,
    }
    return render(request, 'users/detail.html', params)

@login_required
def index(request):    
    users = User.objects.all()
    params = {
        'users': users,
    }
    return render(request, 'users/index.html', params)

@login_required
def detail(request, user_id):
    user = User.objects.get(id=user_id)
    params = {
        'user': user,
    }
    return render(request, 'users/detail.html', params)