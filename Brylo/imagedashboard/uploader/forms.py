from django import forms
from django.contrib.auth.models import User
from .models import ImageUpload
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Your Password'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':' Enter Confirm Password'}))
    mobile = forms.CharField(
    max_length=15,
    widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter Your Mobile Number'
    })
)


    class Meta:
        model = User
        fields = ['username', 'password']

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageUpload
        fields = ['image']