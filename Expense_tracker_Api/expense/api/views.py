from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm, UserLoginForm

from django.contrib.auth import login, authenticate
# Create your views here.


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return redirect('register')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})





        