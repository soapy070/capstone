from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from planner.models import Manager, Team, Member, Location


def welcome(request):
    return render(request, "website/welcome.html",
                  {"team": Team.objects.all(),
                   "manager": Manager.objects.all(),
                   "member": Member.objects.all(),
                   "location": Location.objects.all()})


def date(request):
    return HttpResponse("This page was loaded at " + str(datetime.now()))


def about(request):
    return HttpResponse("Iain Watson Capstone Project.")
