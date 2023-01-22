from django import forms
from .models import Soal

class SoalForm(forms.ModelForm):
    code = forms.Textarea(attrs={'style':'white-space:pre;'})
    class Meta:
        model = Soal
        fields = '__all__'