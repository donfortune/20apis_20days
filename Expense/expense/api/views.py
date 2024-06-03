from django.shortcuts import render, redirect
from .forms import customUserCreationForm, customAuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework_simplejwt.tokens import RefreshToken


# Create your views here.

@login_required
def home(request):
    return render(request, 'home.html')

# def register(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         form = customUserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('login')
#             else:
#                 return redirect('register')
#     else:
#         form = customUserCreationForm()
#     return render(request, 'register.html', {'form': form})

@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        form = customUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the form and retrieve the user object
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')  # Use cleaned_data to get validated data
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                refresh = RefreshToken.for_user(user)

                # Redirect to the desired page after successful registration
                return redirect('home')  # Assuming 'home' is your landing page
            else:
                return redirect('register')  # Redirect back to registration page if authentication fails
    else:
        form = customUserCreationForm()
    return render(request, 'register.html', {'form': form})

@api_view(['POST'])
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)  # Corrected login function call
            refresh = RefreshToken.for_user(user)
            return redirect('home')  # Redirect to home page after successful login
        else:
            return redirect('login')
    else:
        form = customAuthenticationForm()
    return render(request, 'login.html', {'form': form})

@api_view(['POST'])
def user_logout(request):
    logout(request)
    return redirect('login')