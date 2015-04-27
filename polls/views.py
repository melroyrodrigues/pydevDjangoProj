from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render, get_object_or_404
from django.http import Http404

from models import Question
from polls.models import Question
from django.http.response import Http404

def index(request):
  r = RequestContext(request, {'question_list' : Question.objects.all() })
#   t = loader.get_template('polls/index.html')
#   return HttpResponse(t.render(r))
  
  return render( request, 'polls/index.html', r)


def results(req, question_id):
	return HttpResponse('you are looking at the results of question %s' % question_id)

def vote(req, question_id):
	return HttpResponse('You are voting on question id = %s' % (question_id,))
    
# 
# def detail(req, q_id):
#     try:
#         q = Question.objects.get(pk=q_id)
#     except Question.DoesNotExist:
#         raise Http404('Question %s not found' %q_id)
#     
#     return render( req, 'polls/detail.html', { 'question_id': q_id } )



def detail(req, q_id):
    
    q = get_object_or_404(Question, pk=q_id)
    
    return render( req, 'polls/detail.html', { 'question': q } )
