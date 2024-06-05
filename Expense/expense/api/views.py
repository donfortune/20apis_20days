from django.shortcuts import render, redirect
from .forms import customUserCreationForm, customAuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .filters import *



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


@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def get_Expenses(request):
    expenses = Expenses.objects.all()
    serializer = ExpensesSerializer(expenses, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_Expense(request, id):
    expense = Expenses.objects.get(id=id)
    serializer = ExpensesSerializer(expense, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([AllowAny])
def update_Expenses(request, id):
    data = request.data
    expense = Expenses.objects.get(id=id)
    serializer = ExpensesSerializer(expense, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)



@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def get_Products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def expense_list(request)

