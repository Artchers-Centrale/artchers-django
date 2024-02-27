from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail
import random
import string

from .forms import voteForm
from .models import district, OneTimeLinkModel, vote

def randomString(stringLength=20):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def generate_link():
    the_string = randomString(stringLength=20)
    OneTimeLinkModel.objects.create(one_time_code=the_string)
    return the_string

def index(request):
    return render(request, "index.html")

def page_vote(request):
    form = voteForm(request.POST)
    if form.is_valid():
        mail = form.cleaned_data['mail']
        isAlreadyDone = vote.objects.all().filter(mail=mail).count()
        if(isAlreadyDone != 0):
            return HttpResponseRedirect("/AlreadyDone/")
        nom = form.cleaned_data['nom']
        prenom = form.cleaned_data['prenom']
        district = form.cleaned_data['vote']
        key = generate_link()
        send_mail(
            "Confirmation de vote",
            "Bonjour, veuillez confirmer votre vote en cliquant sur ce lien : https://artchers.fr/polls/one_time_link/" +str(key),
            "contact@ic-art.fr",
            [str(mail)],
            fail_silently=False,
        )
        envoiVote = vote(prenom = prenom,nom =nom, mail = mail, vote = district, isConfirmed = False, key = key)
        envoiVote.save()
        return HttpResponseRedirect("/thanks/")
    else:
        form = voteForm()
    context = {'form':form}
    return render(request,'vote.html', context)

def one_time_link(request,access_code=0):
    if OneTimeLinkModel.objects.filter(one_time_code=access_code).exists():
        user = vote.objects.all().filter(key=access_code)[0]
        user.isConfirmed = True
        user.save()

        OneTimeLinkModel.objects.filter(one_time_code=access_code).delete()
        return HttpResponse("Hey, your linked worked. Make sure to download as it won't work again.")

    elif not OneTimeLinkModel.objects.filter(one_time_code=access_code).exists():
        return HttpResponse("Bad or expired link.")
    else:
        return HttpResponse("Bad or expired link.")