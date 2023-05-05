from django.shortcuts import get_object_or_404, redirect, render

from . import forms, models


def index(request):
    return render(request, "orders/index.html")


def add_requester(request):
    form = forms.RequesterForm(request.POST or None)
    if form.is_valid():
        form.save()
        # TODO: Proper redirect required
        return redirect("orders:index")
    return render(request, "orders/add_requester.html", {"form": form})


def edit_requester(request, requester_id):
    requester = get_object_or_404(models.Requester, pk=requester_id)
    form = forms.RequesterForm(request.POST or None, instance=requester)
    if form.is_valid():
        form.save()
        # TODO: Proper redirect required
        return redirect("orders:index")

    context = {"is_edit": True, "form": form, "requester": requester}
    return render(request, "orders/add_requester.html", context)
