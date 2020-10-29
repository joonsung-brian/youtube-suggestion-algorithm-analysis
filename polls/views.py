from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from .models import Choice, Question


def index(request):
    return render(request, 'index.html')


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:6]



class ResultsDone(generic.DeleteView) :

    model = Question
    template_name = 'polls/done.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())





class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
    #투표가 끝나면 출려되는 함수 >>>>>>>>>>>>>>>>>>>작성중...............
    #else 
    #template_name = 'polls/done.html'    



#원본
# class ResultsView(generic.DetailView):
#     model = Question
#     template_name = 'polls/results.html'




def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        if question_id == 1 : 
            return HttpResponseRedirect(reverse('polls:done', args=(question_id,)))

        else  : 
            return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))



def blogMain(request):
    return render(request, 'surveymain.html')

def surveydone(request):
    return render(request, 'surveydone.html')

def about(request):
    return render(request, 'about.html')


def createBlog(request):
 
    if request.method == 'POST':
        form = CreateBlog(request.POST)
 
        if form.is_valid():
            form.save()
            return redirect('surveydone')
        else:
            return redirect('index')
    else:
        form = CreateBlog()
        return render(request, 'startsurvey.html', {'form': form})