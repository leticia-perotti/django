from datetime import datetime
import re
from django import forms
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponseRedirect
from django.urls import reverse, path
from .models import Choice, Question
from .forms import ChoiceForm, QuestionForm
from django.contrib import messages
# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request,'polls/index.html', context)

def results(request, question_id):
    question = Question(pk=question_id)
    return render(request, 'polls/results.html', {'question' : question})

def overall_score(request):
    question_all = Question.objects.all()
    question_id = Choice.objects.filter(pk=question_all)

    return render(request, 'polls/overall_score.html', {
        'question_all': question_all,
        'question_id':question_id
    })

def vote(request, question_id):
    question = get_object_or_404(Question, pk = question_id)

    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except KeyError:
        return render(request, 'polls/vote.html', {
            'question': question,
            'error_message': "Você não escolheu uma pergunta!!"
        })
    else:
        selected_choice.vote += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def insert(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)

        if form.is_valid():
            question = form.save(commit=False)
            question.pub_date = datetime.today()
            question.save()

            return HttpResponseRedirect(reverse('polls:insert_choice', args=(question.id,)))
    
    else:
        form = QuestionForm()
        return render(request, 'polls/insert.html', {'form' : form})
    
def insert_choice(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    if request.method == 'POST':
        form = ChoiceForm(request.POST)

        if form.is_valid():
            choice = form.save(commit=False)
            choice.question = question
            choice.save()
            
            
            return HttpResponseRedirect(reverse('polls:insert_choice', args=(question.id,)), "Dados inseridos")
    
    else:
        form = ChoiceForm()
        return render(request, 'polls/insert_choice.html', {'form' : form})