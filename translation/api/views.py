from orders.models import Company, Requester
from rest_framework import viewsets

from .serializers import CompanySerializer, RequesterSerializer


class RequesterViewSet(viewsets.ModelViewSet):
    """CRUD for Requesters of translation."""
    queryset = Requester.objects.all()
    serializer_class = RequesterSerializer


class CompanyViewSet(viewsets.ModelViewSet):
    """CRUD for Companies related to Documents."""
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
