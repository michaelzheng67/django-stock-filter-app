from django import forms
from .models import tickersymbol

class searchform(forms.ModelForm):
    class Meta:
        model = tickersymbol
        fields = ('ticker',)
