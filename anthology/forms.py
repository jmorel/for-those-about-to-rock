from django import forms
from anthology.models import Contribution


class ContributionForm(forms.ModelForm):
    class Meta:
        model = Contribution
        fields = ['sender', 'message', 'target_type', 'target_slug']
        widgets = {
            'target_slug': forms.HiddenInput(),
            'target_type': forms.HiddenInput(),
        }
