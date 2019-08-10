from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader

from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Questions, Choice


class IndexView(generic.ListView):
    template_name = 'myapp/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Questions.objects.filter(date_public__lte=timezone.now()).order_by('-date_public')[:5]


class DetailView(generic.DetailView):
    model = Questions
    context_object_name = 'question'
    template_name = 'myapp/detail.html'

    def get_queryset(self):
        return Questions.objects.filter(date_public__lte=timezone.now())


class ResultView(generic.DetailView):
    model = Questions
    context_object_name = 'question'
    template_name = 'myapp/results.html'


def vote(request, question_id):
    """
    Processing request
    """
    question = get_object_or_404(Questions, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'myapp/detail.html', {
            'question': question,
            'error_message': "you didn't select a choice"
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('myapp:results', args=(question.id,)))

#  old version funcs index , detail, result

# def index(request):
#     """
#     return last 5 questions, sort by date
#     send in index.html
#     """
#     last_question_list = Questions.objects.order_by('-date_public')[:5]
#     template = loader.get_template('myapp/index.html')
#     context = {
#         'latest_question_list': last_question_list
#     }
#     return HttpResponse(template.render(context, request))
#
#
# def detail(request, question_id):
#     """
#     return 404 if object does not exist
#     """
#     question = get_object_or_404(Questions, pk=question_id)
#     return render(request, 'myapp/detail.html', {'question': question})
#
#     #  call exception manually:
#     #
#     # try:
#     #     question = Questions.objects.get(pk=question_id)
#     # except Questions.DoesNotExist:
#     #     raise Http404('Question does not exist')
#     # return render(request, 'myapp/detail.html', {'question': question})
#
#
#
#
# def results(request, question_id):
#     """
#     result of processing request
#     """
#     question = get_object_or_404(Questions, pk=question_id)
#     return render(request, 'myapp/results.html', {'question': question,})
