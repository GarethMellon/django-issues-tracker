from django.shortcuts import render

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
    return render(request, "ticket.html")
    

def view_comments(request, id):
    """
    A view that will return all current comments for a ticket
    """
    return render (request, "comments.html")
    
def new_comment(request, id):
    """
    A view that will return a new comment input form
    """
    return render(request, "new_comment.html")