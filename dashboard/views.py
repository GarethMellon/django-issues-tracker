from django.shortcuts import render, redirect
from tickets.models import Ticket
from tickets.forms import TicketUserForm, TicketForm
from tickets.helpers import charge
from django.contrib import messages
from tickets.views import save_form
from django.conf import settings
import stripe


# Create your views here.

def dashboard_page(request):
    key = settings.STRIPE_PUBLISHABLE_KEY
    tickets = Ticket.objects.all()
    ticket = Ticket(request.POST)
    
    if request.method == "POST":
        form = TicketUserForm(request.POST, request.FILES)
        save_form(request, form, ticket, 'new')
        return redirect("/")

    ticketForm = TicketUserForm() 
    return render(request, 'dashboard.html', {'tickets': tickets, 'ticketForm': ticketForm, 'key': key})
