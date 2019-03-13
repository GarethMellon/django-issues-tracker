from django.db import models

# Create your models here.


class Comment(models.Model):
    comment_choices=(
        ('Dev',"Dev"),
        ('User', "User")
        )
    
    ticket = models.ForeignKey('Ticket', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, blank=False)
    comment = models.TextField(blank=True)
    comment_type = models.CharField(max_length=20, choices=comment_choices, blank=False, default="User")
    
    def __str__(self):
        return self.comment
    
    
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
    
    ticket_type = models.CharField(max_length=20, choices = type_choices, blank=False)
    subject = models.CharField(max_length= 256, blank=False)
    description = models.TextField( blank=False)
    email = models.EmailField(max_length=254, blank=False)
    priority = models.CharField(max_length=20, choices=priority_choices, default='Minor', blank=False)
    status = models.CharField(max_length=20, choices=status_choices, default='New', blank=False)
    created = models.DateTimeField(auto_now_add=True, blank=False)
    due_date = models.DateTimeField(null=True, blank=True)
    done_date = models.DateTimeField(null=True, blank=True)
    up_vote = models.IntegerField(default=0, blank=True)
    accept = models.BooleanField(default=False)
    #accept = models.CharField(max_length=4, default="0", choices=(("0","0"),("1","1")), blank=False)
    upload_files = models.FileField(upload_to='upload_files', blank=True)
    
    def __str__(self):
        return self.subject