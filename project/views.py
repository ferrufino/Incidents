from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.shortcuts import render, render_to_response
from project.models import Incident, Account, IncidentSummary, Client, Employee
from django.db import connection
from project.forms import TicketForm, AssignForm
from django.views.generic.edit import FormView, View


# Create your views here.
def index(request):
    usern = request.POST.get('Username','') #trae eel dato de username de la forma
    if not usern: # pongo cosas random por si le das reload y no truene abajo
        usern= "papapapa"
    bol = Account.objects.filter(username = usern) #llenar con el query si existe el usuario
    papa = Account.objects.raw("SELECT * FROM Account where Username=%s and type='Administrator'", [usern])
    papa2 = Account.objects.raw("SELECT * FROM Account where Username=%s and type='Employee'", [usern])
    if len(list(papa)):
        #template = loader.get_template('project/manager.html')
        #return render(request, "project/manager.html", {"table": IncidentSummary.objects.raw("SELECT * FROM IncidentSummary")})
        return HttpResponseRedirect('manager')
    elif len(list(papa2)):
		template = loader.get_template('project/employee.html')
		context = RequestContext(request)
		return HttpResponse(template.render(context))
    else:
        template = loader.get_template('project/index.html')
        context = RequestContext(request)
        return HttpResponse(template.render(context))
    
def prueba(request):
    return HttpResponse("You're in employees view.")
    
def results(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/results.html', {'poll': poll})

class Manager(View):
    template_name = 'project/manager.html'

    def get(self,request):
        return render(request, "project/manager.html", {"table": IncidentSummary.objects.raw("SELECT * FROM IncidentSummary")})
	#return HttpResponse("You're in manager view.")

def employee(request):
    return HttpResponse("You're in employees view.")

def allTickets(request):
    template = loader.get_template('project/allTickets.html')
    #return HttpResponse("You should see every ticket in here")
    return render(request, "project/allTickets.html", {"table2": Incident.objects.all(), "formReg" : RegisterTicket()})

class RegisterTicket(FormView):
    #return HttpResponse("This is the ticket creation form")
    template_name = 'project/registerTicket.html'
    form_class = TicketForm
    success_url = '/index/manager'

    def form_valid(self, form):
        typ = form.cleaned_data['type']
        urg = form.cleaned_data['urgency']
        imp = form.cleaned_data['impact']
        desc = form.cleaned_data['description']
        usern = form.cleaned_data['username']

        cursor = connection.cursor()
        cursor.execute("SELECT ClientID FROM Client WHERE Username=%s", [usern])
        uID = cursor.fetchone()

        cursor2 = connection.cursor()
        cursor2.execute('''INSERT INTO Incident VALUES( 
                        DEFAULT, %s, 'submitted', %s, %s, %s,
                        %s, null, CURDATE()
                        ) ''', [typ, urg, imp, desc, uID])
            
        return super(RegisterTicket, self).form_valid(form);


class AssignEmployee(FormView):
    template_name = 'project/AssignEmployee.html'
    form_class = AssignForm
    success_url = '/index/manager/'

    def form_valid(self, form):
        iID = form.cleaned_data['incidentId']
        usern = form.cleaned_data['username']

        cursor = connection.cursor()
        cursor.execute("SELECT EmpID FROM Employee WHERE Username=%s", [usern])
        uID = cursor.fetchone()

        cursor2 = connection.cursor()
        cursor2.execute('''INSERT INTO IncidentHistory VALUES( 
                        %s, %s, NULL, NULL, NULL, NULL
                        ) ''', [iID, uID])

        
        cursor3 = connection.cursor()
        cursor3.execute("UPDATE Incident SET Status='assigned' WHERE IncidentId=%s", [iID])
            
        return super(AssignEmployee, self).form_valid(form);





