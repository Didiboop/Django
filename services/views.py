from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ServiceRequestForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout as auth_logout

@login_required
def contact(request):
    """
    Handles service requests submitted via the contact form.

    If the form is valid, it saves the service request, displays a success message, 
    and redirects the user to the same page.

    Parameters
    ----------
    request : HttpRequest
        The HTTP request object containing metadata about the request.

    Returns
    -------
    HttpResponse
        Renders the 'contact' page with the form context.
        If the request method is POST and the form is valid, redirects to 'contact'.
    """
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your service request has been submitted. We will contact you soon!')
            return redirect('contact')
    else:
        form = ServiceRequestForm()

    return render(request, 'services/contact.html', {'form': form})

def homepage(request):
    """
    Renders the homepage template.

    Parameters
    ----------
    request : HttpRequest
        The HTTP request object containing metadata about the request.

    Returns
    -------
    HttpResponse
        Renders the 'homepage' template.
    """
    return render(request, 'services/homepage.html')

def services(request):
    """
    Renders the services template.

    Parameters
    ----------
    request : HttpRequest
        The HTTP request object containing metadata about the request.

    Returns
    -------
    HttpResponse
        Renders the 'services' template.
    """
    return render(request, 'services/services.html')

def register(request):
    """
    Handles user registration using the UserCreationForm.

    If the form is valid, the user is registered and logged in, 
    and then redirected to the homepage.

    Parameters
    ----------
    request : HttpRequest
        The HTTP request object containing metadata about the request.

    Returns
    -------
    HttpResponse
        Renders the 'register' template with the form context.
        If the request method is POST and the form is valid, redirects to 'homepage'.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful. You are now logged in!')
            return redirect('homepage')
    else:
        form = UserCreationForm()

    return render(request, 'services/register.html', {'form': form})

def custom_logout(request):
    """
    Logs out the user and redirects to the homepage with a success message.

    Parameters
    ----------
    request : HttpRequest
        The HTTP request object containing metadata about the request.

    Returns
    -------
    HttpResponse
        Redirects to the 'homepage' after logging out the user.
    """
    auth_logout(request)
    messages.success(request, "You have been logged out!")
    return redirect('homepage')

class CustomLoginView(LoginView):
    """
    Custom login view that uses a specific login template.

    Attributes
    ----------
    template_name : str
        The path to the template used for rendering the login page.
    """
    template_name = 'services/login.html'
