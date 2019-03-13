from django.shortcuts import render, get_object_or_404
from .forms import TicketForm, CommentForm
from .models import Ticket, Comment

# Create your views here.


def view_ticket(request, id):
    """
    A view that will return a page with a current ticket
    """
    
    ticket = get_object_or_404(Ticket, pk=id)
    form = TicketForm(request.POST, instance=ticket)
    
    return render(request, "ticket.html", {'form': form})
    

def new_ticket(request):
    """
    A view that will return a page with a new ticket input form
    """
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
    
    form = CommentForm()
    
    return render(request, "new_comment.html", {'form':form})