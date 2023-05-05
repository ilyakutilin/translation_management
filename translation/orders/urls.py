from django.urls import path

from . import views

app_name = "orders"

urlpatterns = [
    # Main page
    path("", views.index, name="index"),
    # Add a requester
    path("requesters/add/", views.add_requester, name="add_requester"),
    path(
        "requesters/<int:requester_id>/edit",
        views.edit_requester,
        name="edit_requester",
    ),
]
