from django.shortcuts import render

# Create your views here.

from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from polls.models import Question, Choice
from django.views.generic import ListView, DetailView

class IndexView(ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"
    def get_queryset(self):
        return Question.objects.all().order_by('-pub_date')
    

class DetailView(DetailView):
    model = Question
    context_object_name = 'question'
    template_name = "polls/detail.html"
    

class ResultsView(DetailView):
    model = Question
    context_object_name = "question"
    template_name = "polls/results.html"
    
    
def vote(request, id):
    question = get_object_or_404(Question, pk=id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        context =  {'question': question, 'error_message': "You didn't select a choice.",}
        return render(request, 'polls/detail.html',context)
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
