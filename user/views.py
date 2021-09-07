from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'index.html')


def user_login(request):
    if request.method == 'GET':
        return render(request, 'user/login.html')
    else:
        return render(request, 'user/login.html')


def user_personal(request):
    if request.method == 'GET':
        return render(request, 'user/personal.html')
    else:
        return render(request, 'user/personal.html')


def user_personal_alt(request):
    if request.method == 'GET':
        return render(request, 'user/personal_alt.html')
    else:
        return render(request, 'user/personal_alt.html')
