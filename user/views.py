from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm, RegisterForm, UserRegistrationForm
from .models import UserModel


def get_dashboard(request):
    return render(request, 'base.html')


def user_profile(request):
    return render(request, 'base.html')


def user_cards(request):
    users = User.objects.all()
    return render(request, 'users/user_list.html', {'users': users})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    # return HttpResponse('Authenticated successfully')
                    return redirect('/user/profile/')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'auth/login.html', {'form': form})


def user_register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(
                user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            # Create the user profile
            UserModel.objects.create(user=new_user)
            return redirect('/profile/')
    else:
        user_form = UserRegistrationForm()
    return render(request, 'auth/register.html', {'form': user_form})
