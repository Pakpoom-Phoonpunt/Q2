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


