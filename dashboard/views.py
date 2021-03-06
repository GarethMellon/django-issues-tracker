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
    """
    Main dashboard view
    """
    key = settings.STRIPE_PUBLISHABLE_KEY
    tickets = Ticket.objects.all().order_by('up_vote', 'created').reverse()
    count_bug = Ticket.objects.filter(ticket_type__contains='Bug').count()
    count_feature = Ticket.objects.filter(ticket_type__contains='Feature').count()

    return render(request, 'dashboard.html', {'tickets': tickets, 'key': key, 'count_bug': count_bug, 'count_feature': count_feature})
