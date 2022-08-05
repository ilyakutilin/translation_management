from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CompanyViewSet, RequesterViewSet, TranslationRequestViewSet

router = DefaultRouter()
router.register('requests', TranslationRequestViewSet, basename='request')
router.register('requesters', RequesterViewSet, basename='requester')
router.register('companies', CompanyViewSet, basename='company')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls.jwt')),
]
