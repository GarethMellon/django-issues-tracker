""" helper function to save form data to be used in the views below """
def save_form(request, form):
    if form.is_valid:
        form.save()
        #messages.success(request, "You're ticket has been saved!")