"""oddaj_rzeczy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from main.views import IndexView, FormView, LoginPage, AccountDetails, RegisterView, UserEdit, DonateFirst, \
    DonateSecond, DonateThird

urlpatterns = [
    path('admin/', admin.site.urls, name="admin-site"),
    path('', IndexView.as_view(), name="main-page"),
    path('form/', FormView.as_view(), name="form"),
    path('register/', RegisterView.as_view(), name="register"),
    path('login/', LoginPage.as_view(), name="login-page"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('account/details/', AccountDetails.as_view(), name="account-details"),
    path('account/edit/', UserEdit.as_view(), name="profile-edit"),
    path('password_change/', auth_views.PasswordChangeView.as_view(), name="change-password"),
    path('password_change/done', auth_views.PasswordChangeDoneView.as_view(), name="password_change_done"),
    path('donates/form/1/', DonateFirst.as_view(), name="first-donate"),
    path('donates/form/2/', DonateSecond.as_view(), name="second-donate"),
    path('donates/form/3/', DonateThird.as_view(), name="third-donate"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
