# django
from django.http import JsonResponse
from django.views.decorators.http import require_POST

# ftatr
from anthology.forms import ContributionForm
from ftatr.utils import is_recaptcha_valid


@require_POST
def index(request):
    form = ContributionForm(request.POST)
    is_recaptcha_valid_result = is_recaptcha_valid(request)
    if form.is_valid() and is_recaptcha_valid_result:
        contribution = form.save()
        contribution.send_notification()
        return JsonResponse({'status': 'success'})
    return JsonResponse({
        'status': 'failure',
        'form_errors': form.errors,
        'is_recaptcha_valid': is_recaptcha_valid_result,
    })
