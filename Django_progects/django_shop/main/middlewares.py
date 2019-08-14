from .models import SubRubric


# in settings context_processor
def main_context_processor(request):
    context = {}
    context['rubrics'] = SubRubric.objects.all()
    return context

