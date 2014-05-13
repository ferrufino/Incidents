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
	
def prueba(request):
    return HttpResponse("You're in employees view.")
	
def results(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/results.html', {'poll': poll})
def manager(request):
	user = request.POST.get('Username','') #trae eel dato de username de la forma
	if not user: # pongo cosas random por si le das reload y no truene abajo
		user= "papapapa";
	bol = Account.objects.filter(username = user) #llenar con el query si existe el usuario
	papa = Account.objects.raw("SELECT * FROM Account where Username=%s",user)
	if len(list(papa)):
		template = loader.get_template('project/manager.html')
		return render(request, "project/manager.html", {"table": Account.objects.raw("SELECT * FROM Account")})
	else:
		template = loader.get_template('project/index.html')
		context = RequestContext(request)
		return HttpResponse(template.render(context))

def employee(request, empid):
    return HttpResponse("You're in employees view.")
