from django.shortcuts import render, get_object_or_404, redirect, reverse, HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate
from django.conf import settings
from .helpers import save_form
from .forms import TicketForm, CommentForm
from .models import Ticket, Comment
from issues_tracker.urls import url

# Create your views here.

def view_ticket(request, id):
    """
    A view and edit that will return a page with a current ticket. 
    """
    ticket = get_object_or_404(Ticket, pk=id)

    if request.method == "POST":
        form = TicketForm(request.POST, request.FILES, instance=ticket)
        if request.user.is_authenticated:
            save_form(request, form)
            return redirect("/")
        elif request.user.is_anonymous:
            ####placeholder for Stripe payment####
            save_form(request, form)
            return redirect("/")
    else:
        form = TicketForm(instance=ticket)
        
    return render(request, "ticket.html", {'form': form, 'ticket': ticket})

def new_ticket(request, type):
    """
    A view that will return a page with a new ticket input form
    """
    if request.method == "POST":
        form = TicketForm(request.POST, request.FILES)
        save_form(request, form)
        return redirect('/')
    
    if type =='Dev':
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
    A view that will return a new comment input form
    """
    if request.method=="POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_ticket', id=id)
    
    form = CommentForm()
    
    return render(request, "new_comment.html", {'form':form})
    
def up_vote(request, id):
    if request.user.is_authenticated:
        ticket = get_object_or_404(Ticket, pk=id)
        ticket.up_vote += 1
        ticket.save()
        return redirect("/")
            
    elif request.user.is_anonymous:
        print("Stripe payment required")
        ticket = get_object_or_404(Ticket, pk=id)
        ticket.up_vote += 1
        ticket.save()
        return redirect("/")
