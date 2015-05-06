from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import render
from contribution.forms import ContributionForm, SourceFormset
from contribution.models import Contribution, Source


def new(request):
    if request.method == 'POST':
        contribution_form = ContributionForm(request.POST)
        if contribution_form.is_valid():
            contribution = contribution_form.save()
            source_formset = SourceFormset(request.POST, instance=contribution)
            if source_formset.is_valid():
                source_formset.save()
                return HttpResponseRedirect(reverse('contribution:success'))
        else:
            source_formset = SourceFormset(request.POST)

    else:
        # check that initial settings are present and valid
        if any([elt not in request.GET for elt in ['target_type', 'target_slug', 'attribute']]) \
                or request.GET.get('target_type') not in [target_type[0] for target_type in Contribution.TYPES]:
            return HttpResponseBadRequest('invalid parameters')

        contribution_form = ContributionForm(initial={key: request.GET.get(key)
                                                      for key in ['target_type', 'target_slug', 'attribute']})
        source_formset = SourceFormset()

    return render(request, 'contribution/new.html.jinja2', {
        'contribution_form': contribution_form,
        'source_formset': source_formset
    })


def success(request):
    return render(request, 'contribution/success.html.jinja2')