from django.shortcuts import render, get_object_or_404
from tickets.models import Ticket
from tickets.forms import TicketStagingForm

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

def staging_ticket(request, id):
    """
    A view that will open a staging ticket
    """
    ticket = get_object_or_404(Ticket, pk=id)
    form = TicketStagingForm(instance = ticket)
    
    return render(request, "staging_ticket.html", {'form': form})