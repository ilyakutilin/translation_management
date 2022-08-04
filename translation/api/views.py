from orders.models import Requester
from rest_framework import viewsets

from .serializers import RequesterSerializer


class RequesterViewSet(viewsets.ModelViewSet):
    """CRUD for Requesters of translation."""
    queryset = Requester.objects.all()
    serializer_class = RequesterSerializer
