from django.urls import path

from . import views

app_name = "orders"

urlpatterns = [
    # Main page
    path("", views.index, name="index"),
    # Add a requester
    path("requesters/add/", views.add_requester, name="add_requester"),
]
