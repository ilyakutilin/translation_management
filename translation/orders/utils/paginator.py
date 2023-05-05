from django.core.paginator import Paginator


def pagination(request, objects, limit):
    paginator = Paginator(objects, limit)
    page_number = request.GET.get("page")
    return paginator.get_page(page_number)
