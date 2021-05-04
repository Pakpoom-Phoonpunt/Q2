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

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


