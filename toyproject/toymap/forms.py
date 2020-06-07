from django import forms
from .models import addr

class addrForm(forms.ModelForm):
    class Meta:
        model = addr
        fields = ('body',)