from django import forms
from . import models


class logins(forms.Form):
    Username = forms.CharField(max_length=15)
    password = forms.CharField(max_length=15,widget=forms.PasswordInput)

class frontpage(forms.ModelForm):
    class Meta:
        model = models.Languages
        fields = ['name', 'creator'] #, 'date_created'


