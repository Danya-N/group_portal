from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages

def index(request):
    pass

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("index")
    else:
        form = UserCreationForm()

    return render(
        request,
        template_name="auth_system/register.html",
        context = {"form": form}
    )

# def login(request):
#     if request.method == "POST":
#         form =  AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get("username")
#             password = form.cleaned_data.get("password")
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect("index")
#             else:
#                 messages.error(request, "Неправильний логін та пароль.")