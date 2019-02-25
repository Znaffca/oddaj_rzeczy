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
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from main.views import IndexView, LoginPage, AccountDetails, RegisterView, UserEdit, DonateFirst, \
    DonateSecond, DonateThird, DonateFourth, DonateFifth, DonateSixth, DonateSummary, UserPackages, PackageDetails, \
    ActivationView

urlpatterns = [
    # admin panel
    path('admin/', admin.site.urls, name="admin-site"),
    # landing page
    path('', IndexView.as_view(), name="main-page"),
    # login/logout/register view
    path('register/', RegisterView.as_view(), name="register"),
    path('login/', LoginPage.as_view(), name="login-page"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            ActivationView.as_view(), name="activate"),
    # user account sites
    path('account/details/', AccountDetails.as_view(), name="account-details"),
    path('account/edit/', UserEdit.as_view(), name="profile-edit"),
    path('account/packages/', UserPackages.as_view(), name="user-packages"),
    re_path(r'^account/packages/(?P<id>(\d)+)', PackageDetails.as_view(), name="package-details"),
    # password change
    path('password_change/', auth_views.PasswordChangeView.as_view(), name="change-password"),
    path('password_change/done', auth_views.PasswordChangeDoneView.as_view(), name="password_change_done"),
    # password reset urls
    path('password_reset/', auth_views.PasswordResetView.as_view(), name="password_reset"),
    path('password_reset/done', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
    # add HelpPackage Form
    path('donates/form/1/', DonateFirst.as_view(), name="first-donate"),
    path('donates/form/2/', DonateSecond.as_view(), name="second-donate"),
    path('donates/form/3/', DonateThird.as_view(), name="third-donate"),
    path('donates/form/4/', DonateFourth.as_view(), name="fourth-donate"),
    path('donates/form/5/', DonateFifth.as_view(), name="fifth-donate"),
    path('donates/form/6/', DonateSixth.as_view(), name="sixth-donate"),
    path('donates/form/summary/', DonateSummary.as_view(), name="donate-summary"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
