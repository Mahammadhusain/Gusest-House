from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordChangeForm,UserChangeForm
from django.contrib.auth.models import User
from django.contrib import messages


# User Login form
class userlogin(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control",'placeholder':'Enter Username'}))
    password = forms.CharField(widget=forms.PasswordInput (attrs={"class":"form-control",'placeholder':'Enter Password'}))
    class Meta:
        model = User
        fields = ["username", "password"]
        


# User registration form
class usercreate(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Password'}))
    class Meta:
        model = User
        fields = ["first_name","last_name","email","username", "password1", "password2","is_active","is_staff","is_superuser"]
        widgets = {
            "first_name":forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Firstname'}),
            "last_name":forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Lastname'}),
            "email":forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter E-Mail'}),
            "username":forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Username'}),
            "password1":forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Password'}),
            "password2":forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Re-Password'}),
            'is_active':forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'is_staff':forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'is_superuser':forms.CheckboxInput(attrs={'class':'form-check-input'}),
        }


class UserEditForm(forms.ModelForm):
    password = None
    class Meta:
        model = User
        fields = ["first_name","last_name","email","username","is_active","is_staff","is_superuser"]
        widgets = {
            "first_name":forms.TextInput(attrs={'class':'form-control'}),
            "last_name":forms.TextInput(attrs={'class':'form-control'}),
            "email":forms.EmailInput(attrs={'class':'form-control'}),
            "username":forms.TextInput(attrs={'class':'form-control'}),
            'is_active':forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'is_staff':forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'is_superuser':forms.CheckboxInput(attrs={'class':'form-check-input'}),
        }


class passchangeForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Old Password'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter New Password'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm New Password'}))
    class Meta:
        model = User
        fields = ['old_password','new_password','new_password_confirmation']
        