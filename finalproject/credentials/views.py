from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views he
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('finalapp:allMovieCat')
        else:
            messages.info(request, 'inavlid credentials')
            return redirect('credentials:login')

    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('finalapp:allMovieCat')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already taken')
                return redirect('credentials:register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email id exists')
                return redirect('credentials:register')
            elif User.objects.filter(first_name=fname).exists():
                messages.info(request, 'firstname already taken')
                return redirect('credentials:register')
            elif User.objects.filter(last_name=lname).exists():
                messages.info(request, 'lastname already taken')
                return redirect('credentials:register')
            else:
                user = User.objects.create_user(username=username, password=password, first_name=fname, last_name=lname,
                                                email=email)
                user.save()
                print('user created')
                return redirect('credentials:login')
        else:
            messages.info('password not matching')
            return redirect('credentials:register')
    return render(request, 'register.html')
