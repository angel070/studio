from django import forms
from .models import   *

class addUserForm(forms.ModelForm):
    class Meta:
        model = RegisterUser
        fields = ('firstName', 'lastName', 'email','userName')
