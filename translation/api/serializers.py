from orders.models import Requester
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator


class RequesterSerializer(serializers.ModelSerializer):
    """Serializer for Requesters."""

    class Meta:
        fields = '__all__'
        model = Requester

        validators = [
            UniqueTogetherValidator(
                message='This Requester already exists.',
                queryset=Requester.objects.all(),
                fields=['name', 'email']
            )
        ]
