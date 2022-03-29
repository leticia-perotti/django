from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    return HttpResponse("Essa é a pergunta de número %s" % question_id)

def results(request, question_id):
    return HttpResponse("Esses são os resultados da pergunta de número %s" % question_id)

def vote(request, question_id):
    return HttpResponse("Você está votando na questão de número %s" %question_id)