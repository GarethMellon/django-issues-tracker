from django.shortcuts import render, get_object_or_404, redirect, reverse, HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate
from django.conf import settings

from .helpers import save_form, send_edit_ticket_email, send_new_ticket_email

from .forms import TicketForm, CommentForm
from .models import Ticket, Comment
from .helpers import up_vote_ticket
from issues_tracker.urls import url

# Create your views here.

def view_ticket(request, id):
    """
    A view and edit that will return a page with a current ticket. We also handle saving edits to a ticket.
    """
    ticket = get_object_or_404(Ticket, pk=id)

    if request.method == "POST":
        form = TicketForm(request.POST, request.FILES, instance=ticket)
        if request.user.is_authenticated:
            save_form(request, form, ticket, 'edit')
            return redirect("/")
        elif request.user.is_anonymous:
            save_form(request, form, ticket, 'edit')
            return redirect("/")
    else:
        form = TicketForm(instance=ticket)
        
    return render(request, "ticket.html", {'form': form, 'ticket': ticket})

def new_ticket(request, type):
    """
    A view that will return a page with a new ticket input form.  We also handle saving a new ticket.
    """
    if request.method == "POST":
        form = TicketForm(request.POST, request.FILES)
        ticket = Ticket(request.POST)
        save_form(request, form, ticket, 'new')
        return redirect('/')
    
    if type =='Dev': #### We need to prep a form depending of we are a Dev or a User, with a Bug or Feature.
        form = TicketForm()
    else:
        form = TicketForm(initial={'ticket_type': type})
    
    if type == 'Feature':
        key = settings.STRIPE_PUBLISHABLE_KEY
        return render(request, "ticket_feature.html", {'form': form, 'key': key})
    else:
        return render(request, "ticket.html", {'form': form})
    
def view_comments(request, id):
    """
    A view that will return all current comments for a ticket
    """
    comments = Comment.objects.filter(ticket=id)
    
    return render (request, "comments.html", {'comments': comments})
    
def new_comment(request, id):
    """
    A view that will return a new comment input form.  We also handle saving a comment as well.
    """
    ticket = get_object_or_404(Ticket, pk=id)
    
    if request.method=="POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            save_form(request, form, ticket, "comment")
            return redirect('view_ticket', id=id)
    
    if request.user.is_authenticated:
        form = CommentForm(initial={'comment_type': 'Dev', 'ticket': ticket.id})
    elif request.user.is_anonymous:
        form = CommentForm(initial={'comment_type': 'User', 'ticket': ticket.id})
        
    
    return render(request, "new_comment.html", {'form':form})
    
def up_vote(request, id):
    """
    up vote of tickets including handleing payment process for feature up votes as anonymous user
    """
    ticket = get_object_or_404(Ticket, pk=id)

    if request.user.is_authenticated:
        up_vote_ticket(request, ticket)
        return redirect("/")
    elif request.user.is_anonymous and ticket.ticket_type=="Feature":
        key = settings.STRIPE_PUBLISHABLE_KEY
        up_vote_flag = True
        return render(request, "up_vote_payment.html", {'id': id,'key': key, 'up_vote_flag': up_vote_flag, 'ticket': ticket})
    else:
        up_vote_ticket(request, ticket)
        return redirect("/")
