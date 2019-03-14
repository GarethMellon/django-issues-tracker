from django.shortcuts import render
from tickets.models import Ticket

# Create your views here.

def dashboard_page(request):
    tickets = Ticket.objects.all()
    return render(request, 'dashboard.html', {'tickets': tickets})
