from django.shortcuts import redirect, get_object_or_404
from django.conf import settings
from django.contrib import messages
import stripe
from tickets.models import Ticket
from tickets.forms import TicketForm

""" helper function to save form data to be used in the views below """
def save_form(request, form):
    if form.is_valid:
        form.save()
        #messages.success(request, "You're ticket has been saved!")
        

""" Fucntion to up vote a ticket """
def up_vote_ticket(ticket):
    ticket.up_vote += 1
    ticket.save()
        
        
"""  function to submit a change on a ticket """
def charge (request, id, up_vote_flag):
    if request.method == 'POST':
        stripe.api_key = settings.STRIPE_SECRET_KEY
        charge = stripe.Charge.create(
            amount=50,
            currency='eur',
            description='IssueTrackerCharge',
            source=request.POST['stripeToken']
            )
    if up_vote_flag :
        ticket = get_object_or_404(Ticket, pk=id)
        up_vote_ticket(ticket)
        messages.success(request, "You're ticket has been saved!")
        return redirect('/')
    else:
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "You're ticket has been saved!")
            
    return redirect('/')
