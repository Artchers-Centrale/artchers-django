from django.shortcuts import render

from django.shortcuts import render

import json

from django.template.response import TemplateResponse

from artchers.models import vote, district

 
 
def custom_app_view(request):
    D = list(district.objects.values_list('id','nom'))
    disList = []
    nbrVote = []
    pourcentVote = []
    nbrVoteTot = vote.objects.filter(isConfirmed=True).count()
    for d in D :
       dis = d[0]
       a = vote.objects.filter(vote=dis, isConfirmed=True).count()
       disList.append(d[1])
       nbrVote.append(a)
    for b in nbrVote:
        pourcentVote.append(b/nbrVoteTot*100)

    context={'nbrVote':json.dumps(nbrVote), 'disList':json.dumps(disList), 'pourcent':json.dumps(pourcentVote)}
    return TemplateResponse(request, 'admin/custom_app_view.html',context)