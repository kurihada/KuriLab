from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'index.html')


def user_register(request):
    if request.method == 'GET':
        return render(request, 'user/register.html')
    else:
        return render(request, 'user/register.html')
