from django import forms

class TicketForm(forms.Form):
    #incidentId = forms.CharField(max_length=10)
    type = forms.CharField(widget=forms.TextInput(), max_length=15)
    urgency = forms.IntegerField()
    impact = forms.IntegerField()
    description = forms.CharField(max_length=100)
    username = forms.CharField(max_length=15)

class AssignEmployee(forms.Form):
    incidentId = forms.IntegerField(widget=forms.TextInput())
    username = forms.CharField(widget=forms.TextInput(), max_length=15)