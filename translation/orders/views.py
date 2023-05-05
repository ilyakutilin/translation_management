from django.shortcuts import redirect, render

from . import forms


def index(request):
    return render(request, "orders/index.html")


def add_requester(request):
    form = forms.RequesterForm(request.POST or None)
    if form.is_valid():
        requester = form.save()
        requester.save()
        return redirect("orders:index")
    return render(request, "orders/add_requester.html", {"form": form})
