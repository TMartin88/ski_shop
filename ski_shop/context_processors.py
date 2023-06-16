from django.conf import settings

def show_newsletter(request):
    show_newsletter_signup = True  # Set the variable to True or False based on your logic

    return {'show_newsletter_signup': show_newsletter_signup}
