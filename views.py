from django.contrib.auth import authenticate, logout, login
from django.shortcuts import render, redirect
from .models import *
from .face import face
from .training import training
from .prediction import prediction


# Create your views here.
def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        color = request.POST['color']
        pic = request.FILES['picture']
        # profile_pic = request.FILES['profile_pic']
        face(name)
        training()
        user = User.objects.create_user(username=email, password=password)
        user.save()
        ud = UserDetails(user=user, pic=pic, color=color, name=name)
        ud.save()
        return render(request, 'register.html', {'success': 'success'})
    return render(request, 'register.html')


def logins(request):
    if request.method == "POST":
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('login1')
        else:
            return render(request, 'login.html', {'success': 'success'})
    return render(request, 'login.html')


def login1(request):
    if request.method == "POST":
        user = request.user
        ud = UserDetails.objects.filter(user=user)
        color = request.POST['color']
        if ud[0].color == color:
            return redirect('login2')
        else:
            logout(request)
            redirect('log')
    return render(request, 'login1.html')


def login2(request):
    user = request.user
    ud = UserDetails.objects.filter(user=user)
    pic = ud[0].filename
    return render(request, 'puzzle.html', {'pic': pic})


def login3(request):
    e = prediction()
    user = request.user
    name = UserDetails.objects.filter(user=user)[0].name
    print(e)
    e = e.strip()
    print(name)
    if e == name:
        return redirect('dashboard')
    else:
        return redirect('logout')
    return render(request, 'login3.html')


def dashboard(request):
    d1 = Details.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        social = request.POST['social']
        d = Details.objects.filter(username=username, password=password, social=social)
        if len(d) == 0:
            u = Details(username=username, password=password, social=social)
            u.save()
        else:
            d[0].username = username
            d[0].password = password
            d[0].social = social
            d[0].save()
    return render(request, 'dashboard.html', {'data': d1})


def log(request):
    logout(request)
    return redirect('index')
