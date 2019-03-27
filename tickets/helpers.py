from django.shortcuts import redirect, get_object_or_404
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
import stripe
from tickets.models import Ticket
from tickets.forms import TicketForm

""" helper function to save form data to be used in the views below """
def save_form(request, form, ticket, email_type):
    if form.is_valid:
        try:
            form.save()
            if email_type =='edit':
                send_edit_ticket_email(request, ticket)
            elif email_type =='new':
                send_new_ticket_email(request, ticket)
            elif email_type =='charge':
                send_charge_email(request, ticket)
            elif email_type =='comment':
                send_comment_email(request, ticket)
        except:
            messages.error(request, "There was an error submitting you're request.  Please contact support")
            return redirect('/')

""" Function to up vote a ticket """
def up_vote_ticket(request ,ticket):
    ticket.up_vote += 1
    ticket.save()
    send_upvote_email(request, ticket)
        
"""  function to submit a change on a ticket """
def charge (request, id, up_vote_flag):
    #### Charge the user
    if request.method == 'POST':
        stripe.api_key = settings.STRIPE_SECRET_KEY
        charge = stripe.Charge.create(
            amount=50,
            currency='eur',
            description='IssueTrackerCharge',
            source=request.POST['stripeToken']
            )
    
    #### UP Vote ticket is required.  Other wise we just save the form.
    if up_vote_flag :
        ticket = get_object_or_404(Ticket, pk=id)
        up_vote_ticket(request, ticket)
        messages.success(request, "You're ticket has been saved!")
        return redirect('/')
    else:
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = get_object_or_404(Ticket, pk=id)
            save_form(request, form, ticket, 'charge')
            messages.success(request, "You're ticket has been saved!")
            
    return redirect('/')


"""
EMAIL FUNCTIONS
"""
def send_edit_ticket_email(request, ticket):
    subject = 'Your ticket has been updated!'
    message = 'Thank you for updating a ticket'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [ticket.email,'issue.tracker.django.project@gmail.com']
    send_mail( subject, message, email_from, recipient_list )

def send_new_ticket_email(request, ticket):
    subject = 'Thank you for adding a new ticket!'
    message = 'A new ticket has been added to the dashboard'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [ticket.email,'issue.tracker.django.project@gmail.com']
    send_mail( subject, message, email_from, recipient_list )

def send_charge_email(request, ticket):
    subject = "We have recieved your payment!"
    message = 'You have been charged 50 cent.  Thank you for paying'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [ticket.email, 'issue.tracker.django.project@gmail.com']
    send_mail( subject, message, email_from, recipient_list )
    
def send_upvote_email(request, ticket):
    subject = "You have upvoted a ticket!"
    message = 'Thank you for the upvote.  We will work on your ticket as soon as we can.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [ticket.email, 'issue.tracker.django.project@gmail.com']
    send_mail( subject, message, email_from, recipient_list )

def send_comment_email(request, ticket):
    subject = "You comment has been added!!"
    message = 'Thank you commenting on a ticket.  The development team have been notified'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [ticket.email, 'issue.tracker.django.project@gmail.com']
    send_mail( subject, message, email_from, recipient_list )
