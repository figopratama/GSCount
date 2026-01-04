from django.shortcuts import render, redirect
from django.http import HttpResponse
<<<<<<< HEAD
# from django.contrib.auth import login, authenticate, logout
# from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth.decorators import login_required
# from .forms import RegisterForm, LoginForm
=======
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, LoginForm
>>>>>>> origin/main

def team(request):
    return render(request, 'team.html')

def partner(request):
    return render(request, 'partner.html')

def style(request):
    return render(request, 'style.html')

def home(request):
    return render(request, 'home.html')
<<<<<<< HEAD
  
def upload(request):
    return render(request, 'upload.html')
=======


# Generate triangle
def generate_triangle(n):
    str_n = str(n)
    result = []
    for i in range(len(str_n)):
        # Take the ith character and pad the rest with zeros
        line = str_n[i] + "0" * (len(str_n) - i - 1)
        result.append(line)
    return result

# Generate odd number (ganjil)
def generate_odd_number(n):
    return [x for x in range(1, n+1) if x % 2 != 0]

# Generate prime number (bilangan prima)
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_prime_number(n):
    return [x for x in range(2, n+1) if is_prime(x)]


def index(request):
    result = []
    if request.method == "POST":
        try:
            n = int(request.POST.get("number"))
            if "triangle" in request.POST:
                result = generate_triangle(n)
            elif "odd" in request.POST:
                result = generate_odd_number(n)
            elif "prime" in request.POST:
                result = generate_prime_number(n)
            print(result)
        except ValueError:
            result = ["Enter a valid number!"]
    return render(request, "index.html", {"result": result})

    


# def upload(request):
#     return render(request, 'upload.html')
>>>>>>> origin/main

# def register(request):
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('home')
#     else:
#         form = RegisterForm()
#     return render(request, 'register.html', {'form': form})

# def login_view(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('home')
#             else:
#                 return render(request, 'login.html', {'form': form, 'error': 'Invalid username or password'})
#     else:
#         form = LoginForm()
#     return render(request, 'login.html', {'form': form})

# @login_required
# def logout(request):
#     logout(request)
#     return redirect('login')