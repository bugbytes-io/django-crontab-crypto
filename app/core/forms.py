from django import forms
from .models import Crypto

class CryptoForm(forms.Form):
    name = forms.ModelChoiceField(
        queryset=Crypto.objects.all(),
        initial=Crypto.objects.first()
    )