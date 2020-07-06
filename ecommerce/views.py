from django.shortcuts import render, redirect
from .forms import ContactForm, LoginForm

from django.contrib.auth import authenticate, login


def home_page(request):
    return render(request, 'index.html', context={"text": "Hello from Index Page"})

def login_page(request):
    form = LoginForm(request.POST or None)
    context = {"form": form}

    if form.is_valid():
        print(form.cleaned_data)
        user = authenticate(username=form.cleaned_data.get("username"), password=form.cleaned_data.get("password"))
        print(request.user.is_authenticated)
        if user is not None:
            login(request, user=user)
            print(request.user.is_authenticated)
            # context["form"] = LoginForm()
            redirect("/login")
        else:
            print("Error")
    # No backend authenticated the credentials
    return render(request=request, template_name="auth/login.html", context= context )

def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    if contact_form.is_valid():
            print(contact_form.cleaned_data)
    return render(template_name='contact/view.html', request=request, context={"form": contact_form})
