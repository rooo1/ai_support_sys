from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("", views.home, name="home"),
    path("create/", views.create_ticket, name="create_ticket"),
    path("update/<int:ticket_id>/", views.update_ticket_status, name="update_ticket"),
    path("hello/", views.hello_world, name="hello_world"),
]
