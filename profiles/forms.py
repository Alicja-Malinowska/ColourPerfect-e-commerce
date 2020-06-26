from django import forms
from profiles.models import Profile


class AccountForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['owner']