from django import forms

from .models import RegisterForm
from .validators import *

class RegisterFormUp(forms.ModelForm):
    full_Name = forms.CharField(widget=forms.TextInput(attrs = {'class' : 'form-control', 'placeholder': "Enter your Name"}))
    email = forms.CharField(widget=forms.TextInput(attrs = {'class' : 'form-control', 'placeholder': "Enter your Email"}))
    phone_Number = forms.CharField(widget=forms.TextInput(attrs = {'class' : 'form-control', 'placeholder': "Enter your Phone Number"}))
    question = forms.CharField(widget=forms.Textarea(attrs = {'class' : 'que', 'placeholder': "Enter your Question"}))

    class Meta:
        model = RegisterForm
        fields = ['full_Name', 'email', 'phone_Number', 'question']

    def clean_name(self):
        full_Name = self.cleaned_data.get("full_Name")
        if full_Name == "Hello":
            raise forms.ValidationError("%s is not a valid name") %full_Name
        return full_Name
