from django import forms
from .models import Ticket, Comment

"""
Create input froms from display on the front end.
"""

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ('id','ticket_type','email','priority', 'upload_files','subject', 'description')
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment', 'comment_type')