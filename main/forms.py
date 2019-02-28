from django import forms
from django.contrib.auth.models import User


# login form

from main.models import UserProfile, HelpPackage, Towns, HelpType, DeliveredPackage, Institution


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

    def clean_username(self):
        user = self.cleaned_data['username']
        if User.objects.filter(username=user).exists():
            raise forms.ValidationError("Użytkownik o podanej nazwie już istnienie.")
        return user

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

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exclude(id=self.instance.pk):
            raise forms.ValidationError(f"Użytkownik o adresie {email} już istnieje.")
        return email


# DONATE FORMS
# First Donate

class DonateFirstForm(forms.ModelForm):
    class Meta:
        model = HelpPackage
        fields = ('usable_clothes', 'useless_clothes', 'toys', 'books', 'others')

    def clean(self):
        values = []
        for field in DonateFirstForm.Meta.fields:
            values.append(self.cleaned_data[field])
        if True not in values:
            raise forms.ValidationError("Musisz wybrać przynajmniej jedno pole!")
        return self.cleaned_data


# Second Donate

class DonateSecondForm(forms.ModelForm):
    class Meta:
        model = HelpPackage
        fields = 'bags',
        widgets = {'bags': forms.NumberInput}


# Third Donate - Search Form

class DonateThirdSearch(forms.Form):
    city = forms.ModelChoiceField(queryset=Towns.objects.all(), required=True)
    help = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=HelpType.objects.all(),
                                          required=False)
    institution = forms.CharField(widget=forms.Textarea(attrs={"rows": '4'}), required=False)


# Fourth Donate

class InstitutionSelectForm(forms.Form):
    institution = forms.MultipleChoiceField(widget=forms.RadioSelect)


# Fifth Donate - Add addresess and additional informations

class DonateAddressAdd(forms.ModelForm):
    class Meta:
        model = HelpPackage
        fields = ('street', 'city', 'post_code', 'phone_num', 'date', 'time', 'comments')
        widgets = {
            'post_code': forms.TextInput(attrs={"pattern": "[0-9]{2}\-[0-9]{3}"}),
            'phone_num': forms.TextInput(attrs={"type": "tel", "pattern": "[0-9]{3}-[0-9]{3}-[0-9]{3}"}),
            'date': forms.DateInput(attrs={"type": "date", "name": "date"}),
            'time': forms.TimeInput(attrs={"type": "time", "name": "time"}),
            'comments': forms.Textarea(attrs={"rows": "5"}),
        }


class DeliveredForm(forms.ModelForm):
    class Meta:
        model = DeliveredPackage
        fields = 'delivered',
        widgets = {'delivered': forms.CheckboxInput}
