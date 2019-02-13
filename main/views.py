from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View


# landing page
from main.forms import LoginForm


class IndexView(View):
    def get(self, request):
        return render(request, 'main/index.html')


# form view

class FormView(View):
    def get(self, request):
        return render(request, 'main/form.html')


# login view

class LoginPage(View):

    def get(self, request):
        form = LoginForm()
        return render(request, 'registration/login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'],
                                password=cd['password'])
            if user is not None:
                login(request, user)
                if user.is_superuser:
                    return HttpResponseRedirect('/admin/')
                return redirect('main-page')
        return render(request, 'registration/login.html', {'form': form})
