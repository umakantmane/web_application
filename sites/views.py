from django.shortcuts import render, redirect
from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from sites.forms import LoginForm


def userRegistration(request):

    if request.user.username:

        return redirect(userDashBoard)

    form = UserCreationForm()
    message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            #form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = User()
            user.username = username
            user.set_password(password)
            #user.password = password
            user.save()
            message = 'Registrstion done successfully!'
    return render(
        request,
        'site/registration.html',{
          'form':form,
          'msg':message
        }
    )

def userLogin(request):

    if request.user.username:

        return redirect(userDashBoard)

    form = LoginForm()
    message  = ''
    if request.method == 'POST':

        form = LoginForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(
                username=username,
                password=password
            )
            if user is None:
                message = 'Invalid login details'
            else:

                login(request, user)
                request.session['city'] = 'Banaglore'
                request.session['address'] = 'BTM'
                return redirect(userDashBoard)



    return  render(
        request,
        'site/login.html',{
            'form':form,
            'msg':message
        }
    )

def userDashBoard(request):

    return render(request, 'site/dashboard.html')

def userLogout(request):

    logout(request)

    return redirect(userLogin)

