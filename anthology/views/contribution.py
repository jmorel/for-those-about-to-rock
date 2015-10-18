from django.views.decorators.http import require_POST
from anthology.forms import ContributionForm


@require_POST
def index(request):
    contribution_form = ContributionForm(request.POST)
    return contribution_form
