from anthology.forms import ContributionForm


def contribution_form(target):
    return ContributionForm(initial={
        'target_type': target.contribution_type,
        'target_slug': target.slug,
    })
