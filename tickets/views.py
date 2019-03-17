from django.shortcuts import render, get_object_or_404, redirect, reverse, HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate
from django.core.files.storage import FileSystemStorage
from .forms import TicketForm, CommentForm
from .models import Ticket, Comment
from issues_tracker.urls import url


""" helper function to save form data to be used in the views below """
def save_form(request, form):
    if form.is_valid:
        form.save()
        messages.success(request, "You're ticket has been saved!")

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

def new_ticket(request):
    """
    A view that will return a page with a new ticket input form
    """
    if request.method == "POST":
        form = TicketForm(request.POST, request.FILES
        )
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
            
    form = TicketForm() 
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
