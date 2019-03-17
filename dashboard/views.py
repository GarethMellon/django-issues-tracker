from django.shortcuts import render, redirect
from tickets.models import Ticket
from tickets.forms import TicketUserForm
from tickets.views import save_form

# Create your views here.

def dashboard_page(request):
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
    return render(request, 'dashboard.html', {'tickets': tickets, 'ticketForm': ticketForm})
