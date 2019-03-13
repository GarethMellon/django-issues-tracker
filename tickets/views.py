from django.shortcuts import render
from .forms import TicketForm, CommentForm

# Create your views here.


def view_ticket(request, id):
    """
    A view that will return a page with a current ticket
    """
    return render(request, "ticket.html")
    

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
    return render (request, "comments.html")
    
def new_comment(request, id):
    """
    A view that will return a new comment input form
    """
    
    form = CommentForm()
    
    return render(request, "new_comment.html", {'form':form})