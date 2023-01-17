from django import forms
from .models import Soal

class SoalForm(forms.ModelForm):
    class Meta:
        model = Soal
        fields = '__all__'