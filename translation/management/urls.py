from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("orders.urls", namespace="orders")),
    path("admin/", admin.site.urls),
]
