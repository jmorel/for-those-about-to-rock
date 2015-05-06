from django.forms import ModelForm, inlineformset_factory, HiddenInput
from contribution.models import Contribution, Source


class ContributionForm(ModelForm):
    class Meta:
        model = Contribution
        fields = '__all__'
        help_texts = {
            'content': "The data you want to contribute",
            'contact': "Give us an email or a twitter handle and we'll give you a shoutout when your contribution is live"
        }
        widgets = {
            'target_type': HiddenInput,
            'target_slug': HiddenInput,
            'attribute': HiddenInput,
            'status': HiddenInput
        }

    def get_model(self):
        pass


SourceFormset = inlineformset_factory(Contribution, Source,
                                      extra=0,
                                      validate_min=True,
                                      min_num=1)
