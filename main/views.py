from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from main.forms import LoginForm, AddUserForm, UserEditForm, ProfileForm, DonateFirstForm, DonateSecondForm
from main.models import UserProfile


# landing page


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
                return redirect('account-details')
        return render(request, 'registration/login.html', {'form': form})


# Register to app

class RegisterView(View):

    def get(self, request):
        form = AddUserForm()
        return render(request, 'main/register.html', {'form': form})

    def post(self, request):
        form = AddUserForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            UserProfile.objects.create(user=new_user)
            return render(request, "main/register_done.html", {"new_user": new_user})
        return render(request, 'main/register.html', {"form": form})


# Account details

class AccountDetails(LoginRequiredMixin, View):

    def get(self, request):
        profile = UserProfile.objects.get(user=request.user)
        return render(request, 'main/profile.html', {"user": request.user, "profile": profile})


# Account Edit View

class UserEdit(LoginRequiredMixin, View):

    def get(self, request):
        user_form = UserEditForm(instance=request.user)
        user_profile_form = ProfileForm(instance=request.user.userprofile)
        return render(request, 'main/profile_edit.html', {"user_form": user_form, "user_profile": user_profile_form})

    def post(self, request):
        user_form = UserEditForm(instance=request.user, data=request.POST)
        user_profile_form = ProfileForm(instance=request.user.userprofile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and user_profile_form.is_valid():
            user_form.save()
            user_profile_form.save()
            return HttpResponseRedirect('/account/details/')
        return render(request, 'main/profile_edit.html', {"user_form": user_form, "user_profile": user_profile_form})


# Donates Views:::

# FIRST

class DonateFirst(View):

    def get(self, request):
        if 'form' in request.session:
            form = DonateFirstForm(initial=request.session['form'])
        else:
            form = DonateFirstForm()
        return render(request, 'main/form_1.html', {"form": form})

    def post(self, request):
        form = DonateFirstForm(data=request.POST)
        if form.is_valid():
            s = form.cleaned_data
            request.session['form'] = {
                'usable_clothes': s['usable_clothes'],
                'useless_clothes': s['useless_clothes'],
                'books': s['books'],
                'toys': s['toys'],
                'others': s['others'],
            }
            return redirect('second-donate')
        return render(request, 'main/form_1.html', {"form": form})


# SECOND

class DonateSecond(View):

    def get(self, request):
        form = DonateSecondForm()
        return render(request, 'main/form_2.html', {'form': form})

    def post(self, request):
        form = DonateSecondForm(data=request.POST)
        if form.is_valid():
            s = form.cleaned_data
            request.session['bags'] = {'bags': s['bags']}
            return redirect('third-donate')


# THIRD

class DonateThird(View):

    def get(self, request):
        return render(request, 'main/form_3.html')

    def post(self, request):
        pass