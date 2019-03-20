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
    
    if request.method == "POST":
        form = TicketUserForm(request.POST, request.FILES)
        if request.user.is_authenticated:
            save_form(request, form)
            return redirect("/")
            
        elif request.user.is_anonymous and form.data["ticket_type"]=="Feature":
            print("Stripe payment required")
            save_form(request, form)
            return redirect("/")
        else:
            save_form(request, form)
            return redirect("/")
            
    ticketForm = TicketUserForm() 
    return render(request, 'dashboard.html', {'tickets': tickets, 'ticketForm': ticketForm, 'key': key})
