from django import forms
from .models import Account
class AccountForm(forms.Form):
    GENDER_CHOICE = (
        ('male','male'),
        ('female','female')
    )
    first_name = forms.CharField(max_length=25)
    last_name = forms.CharField(max_length=50)
    gender = forms.ChoiceField(choices=GENDER_CHOICE,widget=forms.RadioSelect)
    phone = forms.CharField(max_length=13)
    address = forms.CharField(max_length=250,widget=forms.Textarea)