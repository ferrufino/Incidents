from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render, render_to_response
from project.models import Incident, Account, IncidentSummary, Client
from django.db import connection
from project.forms import TicketForm


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
    usern = request.POST.get('Username','') #trae eel dato de username de la forma
    if not usern: # pongo cosas random por si le das reload y no truene abajo
        usern= "papapapa"
    bol = Account.objects.filter(username = usern) #llenar con el query si existe el usuario
    papa = Account.objects.raw("SELECT * FROM Account where Username=%s", [usern])
    if len(list(papa)):
        template = loader.get_template('project/manager.html')
        return render(request, "project/manager.html", {"table": IncidentSummary.objects.raw("SELECT * FROM IncidentSummary")})
    else:
        template = loader.get_template('project/index.html')
        context = RequestContext(request)
        return HttpResponse(template.render(context))

def employee(request, empid):
    return HttpResponse("You're in employees view.")

def allTickets(request):
    template = loader.get_template('project/allTickets.html')
    #return HttpResponse("You should see every ticket in here")
    return render(request, "project/allTickets.html", {"table2": Incident.objects.all()})

def registerTicket(request):
    #return HttpResponse("This is the ticket creation form")
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            iID = form.cleaned_data['IncidentId']
            type = form.cleaned_data['type']
            urg = form.cleaned_data['urgency']
            imp = form.cleaned_data['impact']
            desc = form.cleaned_data['description']
            usern = form.cleaned_data['username']

            uID = Client.objects.raw("SELECT ClientID FROM CLient WHERE Username=%s", [usern])

            cursor = connection.cursor()
            cursor.execute('''INSERT INTO Incident VALUES( 
                           %s, %s, 'submitted', %s, %s, %s,
                           %s, null, CURDATE()
                           ) ''', [iID, type, urg, imp, desc, uID])
            return HttpResponseRedirect('/project/allTickets')
    else:
        form = TicketForm()

    return render(request, 'project/registerTicket.html', {'form': form,})






