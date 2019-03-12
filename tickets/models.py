from django.db import models

# Create your models here.

    
class Comment(models.Model):
    comment_choices=(
        ('Dev',"Dev"),
        ('User', "User")
        )
    
    ticket_ref = models.ForeignKey('Ticket', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, blank=False)
    comment = models.TextField(blank=False)
    comment_type = models.CharField(max_length=10, choices=comment_choices, blank=False)
    
    
class Ticket(models.Model):
    type_choices = (
        ('Bug', "Bug"), 
        ('Feature',"Feature")
        )
        
    priority_choices = (
        ('Minor', "Minor"), 
        ('Normal', "Normal"), 
        ('High', "High"), 
        ('Critical', "Critical")
        )
        
    status_choices = (
        ('New', "New"), 
        ('Accepted', "Accepted"), 
        ('Reject', "Reject"), 
        ('Active', "Active"), 
        ('Complete', "Complete")
        )
    
    ticket_type = models.CharField(max_length=10, choices = type_choices, blank=False)
    subject = models.CharField(max_length= 256, blank=False)
    description = models.TextField( blank=False)
    email = models.EmailField(max_length=254, blank=False)
    priority = models.CharField(max_length=10, choices=priority_choices, default='Minor', blank=False)
    status = models.CharField(max_length=10, choices=status_choices, default='New', blank=False)
    created = models.DateTimeField(auto_now_add=True, blank=False)
    due_date = models.DateTimeField(blank=True)
    done_date = models.DateTimeField(blank=True)
    up_vote=models.IntegerField(default=0, blank=False)
    accept = models.BinaryField(default=0, blank=False)
    upload_files = models.FileField(upload_to='upload_files', blank=True)
    comments = models.ManyToManyField(Comment)
