from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CompanyViewSet, RequesterViewSet

router = DefaultRouter()
router.register('requesters', RequesterViewSet, basename='requesters')
router.register('companies', CompanyViewSet, basename='companies')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls.jwt')),
]
