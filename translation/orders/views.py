from django.shortcuts import get_object_or_404, redirect, render
from orders.utils.paginator import pagination

from . import forms, models

REQUESTER_LIST_LIMIT = 50


def index(request):
    requesters = models.Requester.objects.all()
    return render(request, "orders/index.html", {"requesters": requesters})


def add_requester(request):
    form = forms.RequesterAddForm(request.POST or None)
    if form.is_valid():
        form.save()
        # TODO: Proper redirect required
        return redirect("orders:index")
    return render(request, "orders/add_requester.html", {"form": form})


def edit_requester(request, requester_id):
    requester = get_object_or_404(models.Requester, pk=requester_id)
    form = forms.RequesterEditForm(request.POST or None, instance=requester)
    if form.is_valid():
        form.save()
        # TODO: Proper redirect required
        return redirect("orders:index")

    context = {"is_edit": True, "form": form, "requester": requester}
    return render(request, "orders/add_requester.html", context)


def list_requesters(request):
    requester_list = models.Requester.objects.all()
    page_obj = pagination(request, requester_list, REQUESTER_LIST_LIMIT)
    context = {"page_obj": page_obj}
    return render(request, "orders/list_requesters.html", context)
