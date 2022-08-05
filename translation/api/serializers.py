from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from core.utils import utils
from orders.models import Company, Requester, TranslationRequest


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


class CompanySerializer(serializers.ModelSerializer):
    """Serializer for Companies."""

    class Meta:
        fields = '__all__'
        model = Company

    def validate_name(self, value):
        """Check if the company name meets the naming requirements."""
        if not utils.company_name_is_correct(value):
            raise serializers.ValidationError(
                'For company name please use Latin alphabet, in upper case, '
                'without the type of legal entity (i.e. no "LLC" and the like)'
            )
        return value


class TranslationRequestSerializer(serializers.ModelSerializer):
    """Serializer for Translation Requests."""

    class Meta:
        fields = ('requester', 'received', 'email_subject', 'tn_no',
                  'requested_date', 'strict_deadline', 'comments',
                  'current_stage', 'submitted', 'submitter', 'status',)
        model = TranslationRequest
