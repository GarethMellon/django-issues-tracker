from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings

from .models import Contact
from .forms import ContactForm
from django.contrib import messages

# Create your views here.

def contact_us(request):
    """
    A view that will open the contact us page, and allow a user to submit a complaint via a from
    """
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid:
            form.save()
            
            subject = 'A customer has logged a complaint'
            message = 'A customer has logged a complain.  Please log in and check the complains section for the details'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = ['issue.tracker.django.project@gmail.com']
            send_mail( subject, message, email_from, recipient_list )
            
            return redirect("contact_success")
        
    form = ContactForm()
    return render(request, "contact.html", {'form':form})
    
def contact_success(request):
    """
    A view that returns a contact success page
    """
    return render(request, "contact_success.html")
    
def complaints(request):
    """
    A view that returns a list of customer complaints
    """
    complaints = Contact.objects.all()
    return render(request, "complaints.html", {'complaints': complaints})