from django import forms
from .models import Account

class AccountForm(forms.ModelForm):
    GENDER_CHOICES = (
        ('آقا','آقا'),
        ('خانم','خانم')
    )
    phone = forms.CharField(max_length=11,required=True)
    gender = forms.ChoiceField(choices=GENDER_CHOICES,widget=forms.RadioSelect)
    address = forms.CharField(max_length=250,widget=forms.Textarea)
