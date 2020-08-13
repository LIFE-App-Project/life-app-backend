from django import forms
from django .contrib.auth.models import User
from .models import Profile


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password Repeat', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'username')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("Passwords don't match!")
        return cd['password2']


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email Address'
        }

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('photo', 'sex', 'country', 'state', 'mobile_1', 'mobile_2',
                    'education_level', 'date_of_birth', 'description')
        labels = {
            'photo': 'Profile Photo',
            'sex': 'Sex',
            'country': 'Country',
            'state': 'State/Region',
            'mobile_1': 'Mobile Number',
            'mobile_2': 'Other Number',
            'education_level': 'Highest Educational level',
            'description': 'About me'
        }



