from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def login(request):
    return render(request, 'core/login.html')

def singin(request):
    return render(request, 'core/singin.html')

def cat(request):
    return render(request, './viewsNav/cat.html')

def dog(request):
    return render(request, 'core/viewsNav/dog.html')

def bird(request):
    return render(request, 'core/viewsNav/bird.html')

def exotic(request):
    return render(request, 'core/viewsNav/exotic.html')

