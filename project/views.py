from project.models import Account
from django.http import HttpResponse
from django.shortcuts import render
from django.db import connection

# Create your views here.
def index(request):
    #return HttpResponse("Hello, world. You're at the login index.")
    cursor = connection.cursor()
    cursor.execute('select* from Account')
    query = 'select* from Account'
    #return render(cursor.fetchall())
    return render(Account.objects.raw(query))

def employee(request):
    return HttpResponse("Hello, world. You're at the employee view.")

def worker(request, empid):
    return HttpResponse("Hello, world. You're at the worker view." )
