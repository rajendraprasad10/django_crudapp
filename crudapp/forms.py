from django import forms
from django.forms import ModelForm
from .models import CrudData
class CrudForm(forms.ModelForm):
    class Meta:
        model  = CrudData
        fields =  '__all__'