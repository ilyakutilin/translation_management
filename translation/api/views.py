from orders.models import Company, Requester, TranslationRequest
from rest_framework import viewsets

from .serializers import (CompanySerializer, RequesterSerializer,
                          TranslationRequestSerializer)


class RequesterViewSet(viewsets.ModelViewSet):
    """CRUD for Requesters of translation."""
    queryset = Requester.objects.all()
    serializer_class = RequesterSerializer


class CompanyViewSet(viewsets.ModelViewSet):
    """CRUD for Companies related to Documents."""
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class TranslationRequestViewSet(viewsets.ModelViewSet):
    """CRUD for Translation Requests."""
    queryset = TranslationRequest.objects.all()
    serializer_class = TranslationRequestSerializer
