from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Entro a index.")

def manager(request, adminid):
    return HttpResponse("You're in admin view.")

def employee(request, empid):
    return HttpResponse("You're in employees view.")
