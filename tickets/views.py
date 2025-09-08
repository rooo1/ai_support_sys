from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from tickets.gemini_helper import generate_ticket_reply
from .forms import TicketForm, LoginForm
from .models import Ticket

def login_view(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect("login")

@login_required
def home(request):
    tickets = Ticket.objects.filter(user=request.user)
    if request.user.is_staff:  # admin can see all
        tickets = Ticket.objects.all()
    return render(request, "home.html", {"tickets": tickets})

@login_required
def create_ticket(request):
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            # generate AI response
            ai_response = generate_ticket_reply(ticket.title, ticket.description)
            ticket.response = ai_response
            ticket.save()
            return redirect("home")
    else:
        form = TicketForm()
    return render(request, "create_ticket.html", {"form": form})

@login_required
def update_ticket_status(request, ticket_id):
    if request.user.is_staff:
        ticket = Ticket.objects.get(id=ticket_id)
        if request.method == "POST":
            status = request.POST.get("status")
            response = request.POST.get("response")
            ticket.response = response
            ticket.status = status
            ticket.save()
            return redirect("home")
        else:
            # auto-suggest Gemini reply if ticket has no response
            if not ticket.response:
                from .gemini_helper import generate_ticket_reply
                ticket.response = generate_ticket_reply(ticket.title, ticket.description)
        return render(request, "update_ticket.html", {"ticket": ticket})
    return redirect("home")

