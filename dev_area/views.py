from django.shortcuts import render
from tickets.models import Ticket

# Create your views here.

def staging_area(request):
    """
    A view that will return all tickets that needs to be verified before dev work starts
    """
    tickets = Ticket.objects.all()
    return render(request, "staging.html", {'tickets': tickets})

def dev_area(request, id):
    """
    A view that will return all tickets that needs to be verified before dev work starts
    """
    return render(request, "development.html")
