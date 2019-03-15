from django.shortcuts import render

# Create your views here.

def staging_area(request):
    """
    A view that will return all tickets that needs to be verified before dev work starts
    """
    return render(request, "staging.html")

def dev_area(request, id):
    """
    A view that will return all tickets that needs to be verified before dev work starts
    """
    return render(request, "development.html")
