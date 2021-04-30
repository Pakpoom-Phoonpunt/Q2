from django.shortcuts import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
import datetime
from .models import Choice, Question
# Create your views here.

def index(request):
    return HttpResponse("<p>HELLOWORLD<p>")


def display(request):
    context = {'latest_question_list': Question.objects.all()}
    return render(request,"polls/index.html",context)

def sortQuestion(request):
    question = Question.objects.all()  # get a question
    sort = request.POST.get('sort') # get a type sort
    if sort == "maxToMinV": #max vote to min vote
        return question.order_by("-allVote")
    elif sort == "minToMaxV": #min vote to max vote
        return question.order_by("allVote")
    elif sort == "lastToOldT": #last time vote to oldest vote
        return question.order_by("-lastVoteTime")
    elif sort == "oldToLastT": #oldest vote to last time vote 
        return question.order_by("lastVoteTime")
    else: #order by time that publish poll
        return question
