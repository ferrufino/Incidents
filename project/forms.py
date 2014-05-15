from django import forms

class TicketForm(forms.Form):
    incidentId = forms.CharField(max_length=10)
    type = forms.CharField(max_length=15)
    urgency = forms.IntegerField()
    impact = forms.IntegerField()
    description = forms.CharField(max_length=100)
    username = forms.CharField(max_length=15)