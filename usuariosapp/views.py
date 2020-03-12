from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth


def register(request):
    if(request.method == 'POST'):
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        password_confirm = request.POST.get('password_confirm', '')
        validated_fields = True
        if(not name.strip() or not email.strip() or not password.strip() or not password_confirm.strip()):
            print('1')
            validated_fields = False
        elif(password != password_confirm):
            print('2')
            validated_fields = False
        print(request.POST)
        if(validated_fields):
            print('3')
            if(not User.objects.filter(email=email)):
                print('4')
                User.objects.create_user(
                    username=name, email=email, password=password).save()
                return redirect('login')
        return redirect('register')
    return render(request, 'register.html')


def login(request):
    if(request.method == 'POST'):
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        validated_fields = True
        if(not email.strip() or not password.strip()):
            validated_fields = False

        if(validated_fields):
            user = User.objects.filter(email=email).first()
            if(user):
                user = auth.authenticate(
                    request, username=user.username, password=password)
                if(user):
                    auth.login(request, user)
                    return redirect('index')
        return redirect('login')
    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('index')


def dashboard(request):
    return render(request, 'dashboard.html')
