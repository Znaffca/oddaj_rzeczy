import json

from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from main.forms import LoginForm, AddUserForm, UserEditForm, ProfileForm, DonateFirstForm, DonateSecondForm, \
    DonateThirdSearch, DonateAddressAdd
from main.models import UserProfile, Towns, HelpType, Institution, HelpPackage


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
            next_step = request.POST.get('next')
            user = authenticate(request, username=cd['username'],
                                password=cd['password'])
            if user is not None:
                login(request, user)
                if user.is_superuser:
                    return HttpResponseRedirect('/admin/')
                else:
                    if next_step != '':
                        return HttpResponseRedirect(next_step)
                    return HttpResponseRedirect('/account/details/')
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

class DonateFirst(LoginRequiredMixin, View):

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

class DonateSecond(LoginRequiredMixin, View):

    def get(self, request):
        if 'bags' in request.session:
            form = DonateSecondForm(initial={'bags': request.session['bags']})
        else:
            form = DonateSecondForm()
        return render(request, 'main/form_2.html', {'form': form})

    def post(self, request):
        form = DonateSecondForm(data=request.POST)
        if form.is_valid():
            s = form.cleaned_data
            request.session['bags'] = s['bags']
            return redirect('third-donate')
        return render(request, 'main/form_2.html', {'form': form})


# THIRD

class DonateThird(LoginRequiredMixin, View):

    def get(self, request):
        if 'search' in request.session:
            city_form = DonateThirdSearch(initial={'city': Towns.objects.get(pk=request.session['search']['city']),
                                                   'help': (HelpType.objects.get(pk=i) for i in request.session['search']['help']),
                                                   'institution': request.session['search']['institution']})
        else:
            city_form = DonateThirdSearch
        return render(request, 'main/form_3.html', {'city_form': city_form})

    def post(self, request):
        city_form = DonateThirdSearch(request.POST)
        if city_form.is_valid():
            s = city_form.cleaned_data
            city = s['city']
            help_list = [obj.id for obj in s['help']]
            request.session['search'] = {
                'city': city.id,
                'help': help_list,
                'institution': s['institution']
            }
            return redirect('fourth-donate')
        return render(request, 'main/form_3.html', {'city_form': city_form})


# FOURTH

class DonateFourth(LoginRequiredMixin, View):

    def get(self, request):
        city_id = request.session['search']['city']
        # help_list = request.session['search']['help']
        # help_types = (HelpType.objects.get(pk=i) for i in help_list)
        search_by_city = Institution.objects.filter(town=Towns.objects.get(pk=city_id))
        return render(request, 'main/form_4.html', {'city_institution': search_by_city})

    def post(self, request):
        i = request.POST.get('organization')
        if i != '':
            request.session['institution'] = i
            return redirect('fifth-donate')
        return redirect('fourth-donate')


# FIFTH

class DonateFifth(LoginRequiredMixin, View):

    def get(self, request):
        if 'address' and 'datetime' in request.session:
            address = dict()
            for key, value in request.session['address'].items():
                address[key] = value
            for key, value in request.session['datetime'].items():
                address[key] = json.loads(value)
            form = DonateAddressAdd(initial=address)
        else:
            form = DonateAddressAdd()
        return render(request, 'main/form_5.html', {"form": form})

    def post(self, request):
        form = DonateAddressAdd(request.POST)
        if form.is_valid():
            s = form.cleaned_data
            date = json.dumps(s['date'], cls=DjangoJSONEncoder)
            time = json.dumps(s['time'], cls=DjangoJSONEncoder)
            request.session['address'] = {
                'street': s['street'],
                'city': s['city'],
                'post_code': s['post_code'],
                'phone_num': s['phone_num'],
                'comments': s['comments'],
            }
            request.session['datetime'] = {
                'date': date,
                'time': time,
            }
            return redirect('sixth-donate')
        return render(request, 'main/form_5.html', {"form": form})


# SIXTH

class DonateSixth(LoginRequiredMixin, View):

    def get(self, request):
        if 'form' and 'bags' and 'institution' and 'address' and 'datetime' in request.session:
            s = request.session
            address = dict()
            for key, value in request.session['address'].items():
                address[key] = value
            for key, value in request.session['datetime'].items():
                address[key] = json.loads(value)
            ctx = {
                'bags': s['bags'],
                'institution': Institution.objects.get(pk=s['institution']),
                'address': address
            }
            return render(request, 'main/form_6.html', ctx)
        else:
            return redirect('first-donate')

    def post(self, request):
        if 'form' and 'bags' and 'institution' and 'address' and 'datetime' in request.session:
            f = request.session['form']
            s = request.session
            address = dict()
            for key, value in request.session['address'].items():
                address[key] = value
            for key, value in request.session['datetime'].items():
                address[key] = json.loads(value)
            HelpPackage.objects.create(usable_clothes=s['usable_clothes'],
                                       useless_clothes=f['useless_clothes'],
                                       toys=f['toys'],
                                       books=f['books'],
                                       others=f['others'],
                                       bags=s['bags'],
                                       institution=Institution.objects.get(pk=s['institution']),
                                       street=address['street'],
                                       city=address['city'],
                                       post_code=address['post_code'],
                                       phone_num=address['phone_num'],
                                       date=address['date'],
                                       time=address['time'],
                                       comments=address['comments'],
                                       user=request.user
                                       )
            request.session.delete()
            return redirect('donate-summary')
        return redirect('first-donate')


