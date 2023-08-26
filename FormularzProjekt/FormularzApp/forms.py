from django import forms
from .models import PK_Przyjecia

class PKPrzyjeciaForm(forms.ModelForm):
    class Meta:
        model = PK_Przyjecia
        fields = '__all__'
