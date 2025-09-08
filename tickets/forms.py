from django import forms
from .models import Ticket
from django.contrib.auth.forms import AuthenticationForm

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ["title", "description"]

class LoginForm(AuthenticationForm):
    pass
