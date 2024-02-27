from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import voteForm
from .models import district

def index(request):
    return render(request, "index.html")

def vote(request):
    form = voteForm(request.POST)
    if form.is_valid():
        return HttpResponseRedirect("/thanks/")
    else:
        form = voteForm()
    context = {'form':form}
    return render(request,'vote.html', context)