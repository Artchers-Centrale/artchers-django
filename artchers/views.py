from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.utils import timezone
import random
import string

from .forms import voteForm, gameForm
from .models import district, OneTimeLinkModel, vote, Pacman, Event, Resultat

def randomString(stringLength=20):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def generate_link():
    the_string = randomString(stringLength=20)
    OneTimeLinkModel.objects.create(one_time_code=the_string)
    return the_string

def index(request):
    result_query = Resultat.objects.all()
    context = {"result":result_query}
    return render(request, "index.html",context)



def page_vote(request):
    district_query = district.objects.all()
    form = voteForm(request.POST)
    successForm = request.GET.get('successForm',False)
    if form.is_valid():
        mail = form.cleaned_data['mail']
        isAlreadyDone = vote.objects.all().filter(mail=mail).count()
        if(isAlreadyDone != 0):
            return redirect("./vote?successForm=AlreadyDone")
        nom = form.cleaned_data['nom']
        prenom = form.cleaned_data['prenom']
        district_vote = form.cleaned_data['vote']
        key = generate_link()
        send_mail(
            "Confirmation de vote",
            "Bonjour, veuillez confirmer votre vote en cliquant sur ce lien : https://artchers.fr/polls/one_time_link/" +str(key),
            "contact@ic-art.fr",
            [str(mail)],
            fail_silently=False,
        )
        envoiVote = vote(prenom = prenom,nom =nom, mail = mail, vote = district_vote, isConfirmed = False, key = key)
        envoiVote.save()
        return redirect("./vote?successForm=True")
    else:
        form = voteForm()
        print(form.errors.as_data())
    context = {'form':form, "successForm":successForm, 'district':district_query}
    return render(request,'vote.html', context)



def one_time_link(request,access_code=0):
    if OneTimeLinkModel.objects.filter(one_time_code=access_code).exists():
        user = vote.objects.all().filter(key=access_code)[0]
        user.isConfirmed = True
        user.save()

        OneTimeLinkModel.objects.filter(one_time_code=access_code).delete()
        return render(request,"confirm.html")

    elif not OneTimeLinkModel.objects.filter(one_time_code=access_code).exists():
        return render(request,"badLink.html")
    else:
        return render(request,"badLink.html")
    
def about(request):
    return render(request,"about.html")

def cgu(request):
    return render(request,"cgi.html")

def game(request):
    form = gameForm(request.POST)
    if form.is_valid():
        pseudo = form.cleaned_data['pseudo']
        score = form.cleaned_data['score']
        print(score)
        envoiGame = Pacman(pseudo = pseudo,score =score, date=timezone.localtime())
        envoiGame.save()
        return redirect("./game?scoreSaved=True")
    else:
        form = gameForm()

    context={"form":form}
    return render(request,"game.html",context)

def event(request):
    event_query = Event.objects.all()
    context={"event":event_query}
    return render(request, "event.html",context)

def trombi(request):
    return render(request,"trombi.html")