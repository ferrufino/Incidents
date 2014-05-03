from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render, render_to_response
from project.models import Incident, Account
from django.db import connection


# Create your views here.
def index(request):
    template = loader.get_template('project/index.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))

def manager(request, adminid):
    template = loader.get_template('project/manager.html')
    return render(request, "project/manager.html", {"table": Account.objects.raw("SELECT * FROM Account")})
    #return HttpResponse("You're in admin view.")

def employee(request, empid):
    return HttpResponse("You're in employees view.")
