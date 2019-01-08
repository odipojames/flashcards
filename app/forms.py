from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Card



class NewCardForm(forms.ModelForm):
    class Meta:
        model = Card
        exclude = ['user','postedon']
        fields = ['title','image']