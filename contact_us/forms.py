from django import forms
from .models import Contact

"""
From for contacting support with complains
"""
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('email', 'details')
