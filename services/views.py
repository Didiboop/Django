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
    Handle service requests submitted via the contact form.
    Displays a success message and redirects to the same page if the form is valid.
    """
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your service request has been submitted. We will contact you soon!')
            return redirect('contact')  # Redirect to the same page to clear the form and show the success message
    else:
        form = ServiceRequestForm()

    return render(request, 'services/contact.html', {'form': form})

def homepage(request):
    """
    Render the homepage template.
    """
    return render(request, 'services/homepage.html')

def services(request):
    """
    Render the services template.
    """
    return render(request, 'services/services.html')

def register(request):
    """
    Handle user registration using the UserCreationForm.
    Logs the user in and redirects to the homepage upon successful registration.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in immediately after registration
            messages.success(request, 'Registration successful. You are now logged in!')
            return redirect('homepage')  # Redirect to homepage after successful registration
    else:
        form = UserCreationForm()

    return render(request, 'services/register.html', {'form': form})

def custom_logout(request):  # Renamed function
    """
    Log out the user and redirect to the homepage with a success message.
    """
    auth_logout(request)  # Call the built-in logout function
    messages.success(request, "You have been logged out!")
    return redirect('homepage')

class CustomLoginView(LoginView):
    """
    Custom login view that uses a specific login template.
    """
    template_name = 'services/login.html'
