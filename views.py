from django.contrib.auth.forms import AuthenticationForm
from .forms import LoginForm
from django.shortcuts import render, redirect #,get_object_or_404
#from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.http import HttpResponse
from .forms import SignupForm, LoginForm
from django.contrib.auth.decorators import login_required

# from .models import Task

@login_required
def welcome_view(request):
    return render(request, 'lgsuccess.html')

#from .models import *
# Create your views here.
def index(request):
    return HttpResponse("Welcome to LGSG App!!!")
def hello(request):
    return HttpResponse("Hello World")

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        messages.error(request, "check is valid or not")
        if form.is_valid():
            #User = form.save(commit=False)  # Don't save immediately
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']

            if User.objects.filter(username=username).exists():
                messages.error(request, "Username is already taken")
                return render(request, "signup.html", {'form': form})#, 'status':'username_exists'})
                
            if User.objects.filter(email=email).exists():
                messages.error(request, "Email is already registered")
                return render(request, "signup.html", {'form': form})

            if password1 != password2:
                messages.error(request, "Passwords do not match")
                return render(request, "signup.html", {'form': form})                

            user= User.objects.create_user(username=username, email=email, password=password1)
            #form.save()
            messages.success(request, "Account created successfully! Please login")
            return redirect("login")
        
        else:
            print("Form Errors:", form.errors.as_data())
            for field, error_list in form.errors.items():
                for error in error_list:
                    messages.error(request, f"{field}: {error}")
            print("Form Errors: ",form.errors)  # Debugging line to check errors

            messages.error(request, "Invalid form submission")
    else:
        form = SignupForm()
    return render(request, "signup.html", {'form': form})  # Show signup form

# def login_view(request):
#     if request.method == 'POST':
#         form = LoginForm(request, data=request.POST) #LoginForm(request.POST)
#         #print("POST data:", request.POST)
    
#         if form.is_valid():
#             #username = form.cleaned_data['username']
#             #password = form.cleaned_data['password']
#             form = AuthenticationForm(request, data=request.POST)
#             username = form.get_user()
#             login(request,username)
#             messages.success(request, "Login successful!")
#             return redirect("lgsuccess")
#             #print("Trying to authenticate...")
#             #print(f"Username: {username}")
#             #print(f"Password: {password}")
#             #print("User exists?", User.objects.filter(username=username).exists())

#             #user = authenticate(request, username=username, password=password)  # 🔍 Check if the password matches
#             #print("Authenticated user:", user)

#             #if user is not None:
#             #    login(request, user)
#             #    messages.success(request, "Login successful!")
#             #    #return redirect("lgsuccess")  # Redirect to success page after login
#             #else:
#             #    messages.error(request, "Invalid username or password")
#         else:
#             for field, error_list in form.errors.items():
#                 for error in error_list:
#                     messages.error(request, f"{field}: {error}")
#             print("Form Errors:", form.errors.as_data())       
#             messages.error(request, "Invalod f s")
#     else:
#         form = LoginForm()
#     return render(request, "login.html", {'form': form})  # Show login form with Captcha



def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)  # Directly using AuthenticationForm
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            remember_me = request.POST.get('remember_me', False)
            # Authenticate user
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                if remember_me:
                    request.session.set_expiry(60*60*42*30)# 30 days
                else:
                    request.session.set_expiry(0)
                messages.success(request, "Login successful!")
                return redirect("lgsuccess")  # Redirect to a success page
            else:
                messages.error(request, "Invalid username or password")
        else:
            # Handle form errors
            for field, error_list in form.errors.items():
                for error in error_list:
                    messages.error(request, f"{field}: {error}")
    else:
        form = LoginForm()  # Initialize the form when the page is loaded

    return render(request, "login.html", {'form': form})


