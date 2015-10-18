from django_jinja import library
from anthology.forms import ContributionForm


@library.global_function
def contribution_form(target):
    return ContributionForm(initial={
        'target_type': target.contribution_type,
        'target_slug': target.slug,
    })
