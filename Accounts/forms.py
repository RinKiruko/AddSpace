from django import forms

from .models import User
from AddList.models import Add


class UserModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('FirstName', 'LastName', 'email', 'password')

    FirstName, LastName, email = [forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))] * 3
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class AddModelForm(forms.ModelForm):
    class Meta:
        model = Add
        exclude = ('Author', 'PostingDate')
