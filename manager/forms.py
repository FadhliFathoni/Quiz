from django import forms
from .models import Soal

class SoalForm(forms.ModelForm):
    class Meta:
        model = Soal
        fields = ['title','description','code','category','course']

class ContohForm(forms.ModelForm):
    class Meta:
        model = Soal
        fields = ['contoh']

        