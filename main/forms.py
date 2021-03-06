from django import forms
from django.contrib.auth.models import User


# login form
from main.models import UserProfile


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username']
        if not User.objects.filter(username=username).exists():
            raise forms.ValidationError('Nieprawidłowa nazwa użytkownika')
        return username


# Registration Form

class AddUserForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput, label="Hasło")
    password2 = forms.CharField(widget=forms.PasswordInput, label="Powtórz hasło")

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_password2(self):
        check = self.cleaned_data
        if check['password'] != check['password2']:
            raise forms.ValidationError('Hasła nie zgadzają się!!!')
        return check['password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(f"Użytkownik o adresie {email} już istnieje.")
        return email


# Edit User Profile forms

class ProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('date_of_birth', 'description', 'photo', 'phone_num')
        widgets = {
            'description': forms.Textarea,
            'date_of_birth': forms.DateInput,
        }


class UserEditForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


