from django.contrib.auth import get_user_model
from django.db import models

from .utils import choices

User = get_user_model()


class TranslationRequest(models.Model):
    """Model for a translation request."""
    # TODO: This will need to be a Foreign Key to the 'Requester' model
    requester = models.CharField(
        'Requester',
        max_length=30,
        help_text='Requester of the translation'
    )
    received = models.DateTimeField(
        'Received Date & Time',
        blank=False,
        null=False,
        help_text=('Translation Request Received Date and Time, '
                   'as per the request email')
    )
    email_subject = models.CharField(
        'Email Subject',
        max_length=100,
        blank=False,
        help_text=('Request Email Subject, without "RE" or "FW". '
                   'Indicate "no subject" if the actual subject is blank.')
    )
    tn_no = models.CharField(
        'Transmittal No.',
        max_length=50,
        blank=True,
        help_text='Transmittal Number as per the DCC info'
    )
    requested_date = models.DateTimeField(
        'Requested Date',
        blank=False,
        null=False,
        help_text=('Date and Time when the translation is requested'
                   'to be provided back to the requester')
    )
    strict_deadline = models.BooleanField(
        'Strict Deadline',
        default=False,
        help_text=('True if the Requested Date and Time are strictly'
                   'determined by the request. False if the Requested Date '
                   'and Time are set internally.')
    )
    # TODO: This can be implemented as a Foreign Key
    # if the stage is a separate model
    current_stage = models.CharField(
        'Request Stage',
        max_length=3,
        choices=choices.REQUEST_STAGE_CHOICES,
        help_text='Current stage of the request'
    )
    submitted = models.DateTimeField(
        'Submission Date',
        blank=True,
        null=True,
        help_text='Date of submission. Not submitted yet if not indicated.'
    )
