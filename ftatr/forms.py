from django import forms
from ftatr.models import ContactMessage


class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['sender', 'subject', 'message']
