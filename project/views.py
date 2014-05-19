from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.shortcuts import render, render_to_response
from project.models import Incident, Account, IncidentSummary, Client, Employee, Administrator, IncidentHistory
from django.db import connection
from project.forms import TicketForm, AssignForm, CloseIncidentForm, IncidentHistoryForm
from django.views.generic.edit import FormView, View
from django.core.urlresolvers import reverse


# Create your views here.
def index(request):
    usern = request.POST.get('Username','') #trae eel dato de username de la forma
    if not usern: # pongo cosas random por si le das reload y no truene abajo
        usern= "papappa"
    bol = Account.objects.filter(username = usern) #llenar con el query si existe el usuario
    #papa = Account.objects.raw("SELECT * FROM Account where Username=%s and type='Administrator'", [usern])
    #papa2 = Account.objects.raw("SELECT * FROM Account where Username=%s and type='Employee'", [usern])
    papa = Administrator.objects.raw("SELECT * FROM Administrator where Username=%s", [usern])
    papa2 = Employee.objects.raw("SELECT * FROM Employee where Username=%s", [usern])
    if len(list(papa)):
        #template = loader.get_template('project/manager.html')
        #return render(request, "project/manager.html", {"table": IncidentSummary.objects.raw("SELECT * FROM IncidentSummary")})
        suffix = str(papa[0].adminid)
        url = 'manager/' + suffix
        return HttpResponseRedirect(url)
    elif len(list(papa2)):
		#template = loader.get_template('project/employee.html')
		#context = RequestContext(request)
		#return HttpResponse(template.render(context))
        suffix = str(papa2[0].empid)
        url = 'employee/' + suffix
        return HttpResponseRedirect(url)
    else:
        template = loader.get_template('project/index.html')
        context = RequestContext(request)
        return HttpResponse(template.render(context))
    
def prueba(request):
    return HttpResponse("You're in employees view.")
    
def results(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/results.html', {'poll': poll})

class ManagerView(View):
    template_name = 'project/manager.html'

    def get(self,request, adminid):
		return render(request, "project/manager.html", {"table": IncidentSummary.objects.raw("SELECT * FROM IncidentSummary"),
														"table2": Incident.objects.all(),
														"closed_incidents": Incident.objects.raw("SELECT * FROM Incident WHERE status='closed'"),
														"open_incidents": Incident.objects.raw("SELECT * FROM Incident WHERE status<>'closed'"),
														"ej1" : Incident.objects.raw("SELECT * FROM Incident WHERE status='closed'"),
														"ej5" : Incident.objects.raw("SELECT * FROM Incident WHERE status='closed'"),
														"ej6" : Incident.objects.raw("SELECT * FROM Incident WHERE status='closed'"),															
														#"ej1": Incident.objects.raw("SELECT * from ej1"),
														"ej2": Incident.objects.raw("SELECT * FROM incident WHERE DateClosed IS NULL AND DateSubmitted <= ALL( SELECT DateSubmitted FROM incident)"),
														"ej3": Incident.objects.raw("SELECT * FROM incident WHERE MONTH(DateSubmitted) = MONTH(NOW())"),
														"ej4": Incident.objects.raw("SELECT * FROM incident ORDER BY TYPE"),
														#"ej5": Incident.objects.raw("select * from ej5"),
														#"ej6": Incident.objects.raw("select * from ej6"),
														"ej7": Incident.objects.raw("SELECT * FROM incident WHERE DateClosed IS NULL AND  urgency >= ALL( SELECT urgency FROM incident)"),
														"ej8": Incident.objects.raw("SELECT* FROM incident WHERE DateClosed IS NULL AND impact >= ALL( SELECT impact FROM incident )"),
														"adminid": adminid})
        #return render(request, "project/manager.html", {"table": IncidentSummary.objects.raw("SELECT * FROM IncidentSummary"),
        #                                                "table2": Incident.objects.all()})

	#return HttpResponse("You're in manager view.")

class EmployeeView(View):
    template_name = 'project/employee.html'
    def get(self,request, empid):
        return render(request, 'project/employee.html', {"assigned_incidents": IncidentHistory.objects.raw("SELECT* FROM IncidentHistory WHERE empid=%s", [empid]),
                                                        "empid": empid})
        #return render(papa in request.GET)


def allTickets(request):
    template = loader.get_template('project/allTickets.html')
    #return HttpResponse("You should see every ticket in here")
    return render(request, "project/allTickets.html", {"table2": Incident.objects.all()})

class RegisterTicket(FormView):
    #return HttpResponse("This is the ticket creation form")
    template_name = 'project/registerTicket.html'
    form_class = TicketForm

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
                        %s, null, CURDATE(), null
                        ) ''', [typ, urg, imp, desc, uID])
            

	

    def post(self, request, adminid):
		typ = request.POST.get('type','')
		urg = request.POST.get('urgency','')
		imp = request.POST.get('impact','')
		desc = request.POST.get('description','')
		usern = request.POST.get('username','')

		cursor = connection.cursor()
		cursor.execute("SELECT ClientID FROM Client WHERE Username=%s", [usern])
		uID = cursor.fetchone()

		cursor2 = connection.cursor()
		cursor2.execute('''INSERT INTO Incident VALUES( 
						DEFAULT, %s, 'submitted', %s, %s, %s,
						%s, null, CURDATE(), null
						) ''', [typ, urg, imp, desc, uID])
		#adminid = request.GET.get('adminid', 'kkjhkjg')
		url = '/index/manager/' + adminid
		return HttpResponseRedirect(url)


class AssignEmployee(FormView):
    template_name = 'project/AssignEmployee.html'
    form_class = AssignForm

    def post(self, request, adminid):
        iID = request.POST.get('incidentId', '')
        usern = request.POST.get('username', '')

        cursor = connection.cursor()
        cursor.execute("SELECT EmpID FROM Employee WHERE Username=%s", [usern])
        uID = cursor.fetchone()

        #count_cursor = connection.cursor()
        #count_cursor.execute("SELECT COUNT(timesWorked) FROM IncidentHistory where EmpID=%s", [uID])
        #count = count_cursor +1


        #cursor2 = connection.cursor()
        #cursor2.execute("INSERT INTO IncidentHistory VALUES(%s, %s, DEFAULT, DEFAULT, NULL, DEFAULT, NULL)", [iID, uID])

        
        cursor3 = connection.cursor()
        cursor3.execute("UPDATE Incident SET Status='assigned', EmpID=%s WHERE IncidentId=%s", [iID, uID])

        url = '/index/manager/' + adminid
        return HttpResponseRedirect(url)


class CloseIncident(FormView):
    #return HttpResponse("This is the ticket creation form")
    template_name = 'project/CloseIncident.html'
    form_class = CloseIncidentForm

    def post(self, request, adminid):
        iID = request.POST.get('closedIncident', '')

        cursor = connection.cursor()
        cursor.execute("UPDATE Incident SET Status='closed' WHERE IncidentId=%s", [iID])

        cursor2 = connection.cursor()
        cursor2.execute("UPDATE Incident SET DateClosed=CURDATE() WHERE IncidentId=%s", [iID])

        url = '/index/manager/' + str(adminid)
        return HttpResponseRedirect(url)

    def form_valid(self, form):
        iID = form.cleaned_data['closedIncident']

        cursor = connection.cursor()
        cursor.execute("UPDATE Incident SET Status='closed' WHERE IncidentId=%s", [iID])

        cursor2 = connection.cursor()
        cursor2.execute("UPDATE Incident SET DateClosed=CURDATE() WHERE IncidentId=%s", [iID])

        return super(RegisterTicket, self).form_valid(form);

class UpdateIncident(FormView):
    #return HttpResponse("This is the ticket creation form")
    template_name = 'project/UpdateIncident.html'
    form_class = IncidentHistoryForm

    def post(self, request, adminid):
        iID = request.POST.get('incidentId', '')
        start = request.POST.get('hourStart', '')
        end = request.POST.get('hourEnd', '')
        conc = request.POST.get('concluded', '')
        desc = request.POST.get('description', '')
        empid = request.POST.get('empId', '')

        #count_cursor = connection.cursor()
        #count_cursor.execute("SELECT COUNT(timesWorked)+1 FROM IncidentHistory where EmpID=%s", [empid])
        #count = int(count_cursor.fetchone()[0])
        #test_cursor = connection.cursor()
        #test_cursor.execute("SELECT COUNT(timesWorked)+1 FROM IncidentHistory WHERE IncidentId=%s AND EmpID=%s", [iID, empid])
        #test = int(test_cursor.fetchone()[0])
        #test = IncidentHistory.objects.raw("SELECT timesWorked FROM IncidentHistory WHERE IncidentId=%s AND EmpID=%s", [iID, empid])[0]

        cursor = connection.cursor()
        #cursor.execute("UPDATE IncidentHistory SET timesWorked=%s, TimeStart=%s, TimeEnd=%s, DateWorked=CURDATE(), description=%s WHERE IncidentId=%s", [test, start, end, desc, iID])
        
        cursor.execute("INSERT INTO IncidentHistory VALUES(%s, %s, DEFAULT, %s, %s, CURDATE(), %s)", [iID, empid, start, end, desc])

        if conc:
            cursor2 = connection.cursor()
            cursor2.execute("UPDATE Incident SET status='solved' WHERE IncidentId=%s", [iID])

        url = '/index/employee/' + empid
        return HttpResponseRedirect(url)







