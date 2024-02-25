from django.shortcuts import render

from .models import district

def index(request):
    district_sel = district.objects.all()
    context = {"district_sel":district_sel}

    return render(request, "index.html", context)