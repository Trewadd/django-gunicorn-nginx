from django.template import loader
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Question, Choice
from django.shortcuts import render, get_object_or_404, reverse

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404('Question not found')
    return render(request, 'polls/detail.html', {'question':question})

def result(request, question_id):
    qustion = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': qustion})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])

    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question':question,
            'error_message': "You didn't select a choice"
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
    return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))