from django import forms
from project.models import Client

class TicketForm(forms.Form):
    #incidentId = forms.CharField(max_length=10)
    type = forms.CharField(widget=forms.TextInput(), max_length=15)
    urgency = forms.IntegerField()
    impact = forms.IntegerField()
    description = forms.CharField(max_length=100)
    username = forms.CharField(max_length=15)
    #adminid = forms.CharField()


class AssignForm(forms.Form):
    incidentId = forms.IntegerField()
    username = forms.CharField(max_length=15)

class IncidentHistoryForm(forms.Form):
    incidentId = forms.IntegerField()
    hourStart = forms.TimeField()
    hourEnd = forms.TimeField()
    concluded = forms.BooleanField()
    description = forms.CharField(max_length=100)

class CloseIncidentForm(forms.Form):
    IncidentID = forms.IntegerField()

class AddClientForm(forms.ModelForm):
    class Meta:
        model = Client
