from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .form import CreateUserForm

# Create your views here
def homePage(request):
    return render(request, 'home.html')

def signup_page(reqest):
    # Check if the user is already authenticated
    if reqest.user.is_authenticated:
        # Redirect to home page if the user is already logged in
        return redirect('home')
    else:
        # Create an instance of the CreateUserForm
        form = CreateUserForm()
        if reqest.method == 'POST':
            # Populate the form with data from the request
            form = CreateUserForm(reqest.POST)
            if form.is_valid():
                # Save the form and create a new user
                form.save()
                # Get the username of the newly created user
                user = form.cleaned_data.get('username')
                # Send a success message
                messages.success(reqest, 'Account was created for ' + user)
                # Redirect to the home page
                return redirect('home')
        # Render the register template with the form
        return render(reqest, 'signup.html', context={'form': form})

def login_page(request):
    """
    Renders the login page and handles user authentication.
    If the user is already authenticated, redirects to the home page.
    """
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')

        return render(request, 'login.html')


@login_required
def logout_user(request):
    """
    Logs out the current user and redirects them to the login page.
    """
    logout(request)
    messages.info(request, "You have been successfully logged out.")
    return redirect('home')