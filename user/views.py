from django.shortcuts import render


def user_profile(request):
    return render(request, 'base.html')
