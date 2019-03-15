from django.shortcuts import render, get_object_or_404, redirect, reverse, HttpResponse
from .forms import TicketForm, CommentForm
from .models import Ticket, Comment
from issues_tracker.urls import url

# Create your views here.


def view_ticket(request, id):
    """
    A view and edit that will return a page with a current ticket
    """
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid:
            form.save()
            return HttpResponse("____SAVED FORM____") ## placeholder code
        else:
            return HttpResponse("_______we post______") ## placeholder code
    else:
        ticket = get_object_or_404(Ticket, pk=id)
        form = TicketForm(instance=ticket)
        
    return render(request, "ticket.html", {'form': form, 'id':ticket.id})
    

def new_ticket(request):
    """
    A view that will return a page with a new ticket input form
    """
    if request.method=="POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return HttpResponse("____we post____") ## placeholder code
            
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