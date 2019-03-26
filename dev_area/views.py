from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from tickets.models import Ticket
from tickets.forms import TicketStagingForm, TicketForm

# Create your views here.

def staging_area(request):
    """
    A view that will return all tickets that needs to be verified before dev work starts
    """
    tickets = Ticket.objects.all().order_by('up_vote', 'created').reverse()
    ticketForm = TicketForm()
    count_bug = Ticket.objects.filter(ticket_type__contains='Bug', accept__contains="0").count()
    count_feature = Ticket.objects.filter(ticket_type__contains='Feature', accept__contains="0").count()
    
    return render(request, "staging.html", {'tickets': tickets, 'ticketForm': TicketForm, 'count_bug': count_bug, 'count_feature': count_feature})
    
def staging_ticket(request, id):
    """
    A view that will open a staging ticket
    """
    ticket = get_object_or_404(Ticket, pk=id)
    form = TicketStagingForm(instance = ticket)
    
    return render(request, "staging-ticket.html", {'form': form, 'ticket': ticket})
    
def staging_accept(request, id):
    
    ticket = get_object_or_404(Ticket, pk=id)
    ticket.accept = 1
    ticket.save()
    messages.success(request, "Ticket accepted for development")
    return redirect("staging")
    
def staging_reject(request, id):
    
    ticket = get_object_or_404(Ticket, pk=id)
    ticket.accept = 0
    ticket.status = "Reject"
    ticket.save()
    messages.success(request, "Ticket rejected for development")
    return redirect("staging")
    
def dev_area(request):
    """
    A view that will return all tickets that needs to be verified before dev work starts
    """
    tickets = Ticket.objects.all().order_by('up_vote', 'created').reverse()
    ticketForm = TicketForm()
    count_bug = Ticket.objects.filter(ticket_type__contains='Bug', accept__contains="1").count()
    count_feature = Ticket.objects.filter(ticket_type__contains='Feature', accept__contains="1").count()
    
    return render(request, "development.html", {'tickets': tickets, 'ticketForm': ticketForm, 'count_bug': count_bug, 'count_feature': count_feature})

def dev_ticket(request, id):
    """
    this view will return a dev ticket
    """
    ticket = get_object_or_404(Ticket, pk=id)
    form = TicketForm(instance=ticket)
    
    return render(request, "development-ticket.html", {'form': form, 'ticket': ticket})

