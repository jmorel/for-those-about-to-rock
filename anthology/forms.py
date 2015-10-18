from django import forms
from anthology.models import Contribution


class ContributionForm(forms.ModelForm):
    class Meta:
        model = Contribution
        fields = ['sender', 'message']
