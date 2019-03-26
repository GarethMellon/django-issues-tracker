from django.shortcuts import render, redirect
from tickets.models import Ticket
from tickets.forms import TicketForm
from tickets.helpers import charge
from django.contrib import messages
from tickets.views import save_form
from django.conf import settings
import stripe


# Create your views here.

def dashboard_page(request):
    key = settings.STRIPE_PUBLISHABLE_KEY
    tickets = Ticket.objects.all()

    return render(request, 'dashboard.html', {'tickets': tickets, 'key': key})
