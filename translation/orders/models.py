from uuid import uuid4

from django.contrib.auth import get_user_model
from django.db import models

from .utils import choices

User = get_user_model()


class Requester(models.Model):
    """Model for the translation requesters."""
    name = models.CharField(
        'Name',
        max_length=50,
        help_text=('Full name of the requester. Whenever possible, '
                   'input first name first, and last name last.')
    )
    email = models.EmailField(
        'Email',
        help_text='Email of the translation requester'
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                name='orders_requester_unique_relationships',
                fields=['name', 'email'],
            )
        ]
        verbose_name = 'Requester'
        verbose_name_plural = 'Requesters'

    def __str__(self):
        return self.name


class TranslationRequest(models.Model):
    """Model for a translation request."""
    requester = models.ForeignKey(
        Requester,
        on_delete=models.RESTRICT,
        related_name='requests',
        verbose_name='Requester',
        help_text='Requester of the translation'
    )
    received = models.DateTimeField(
        'Received Date & Time',
        help_text=('Translation Request Received Date and Time, '
                   'as per the request email')
    )
    email_subject = models.CharField(
        'Email Subject',
        max_length=100,
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
    comments = models.CharField(
        'Comments',
        max_length=100,
        blank=True,
        help_text='Comments to the Request'
    )
    current_stage = models.ForeignKey(
        'Activity',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='Current Stage',
        help_text='Current stage of the request'
    )
    submitted = models.DateTimeField(
        'Submission Date',
        blank=True,
        null=True,
        help_text='Date of submission. Not submitted yet if not indicated.'
    )
    submitter = models.ForeignKey(
        User,
        on_delete=models.RESTRICT,
        related_name='requests',
        blank=True,
        null=True,
        verbose_name='Submitter',
        help_text='Registered user who submitted the request to the requester'
    )
    status = models.CharField(
        'Status',
        max_length=3,
        choices=choices.STATUS_CHOICES,
        default='PND',
        help_text=('Translation Request status,'
                   'selected from the list of the predefined ones')
    )

    class Meta:
        verbose_name = 'Translation Request'
        verbose_name_plural = 'Translation Requests'

    def __str__(self):
        return f'{self.requester.name} - {self.email_subject[:15]}'


class Activity(models.Model):
    """Model for the activity types."""
    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False
    )
    translation_request = models.ForeignKey(
        TranslationRequest,
        on_delete=models.CASCADE,
        related_name='activities',
        verbose_name='Translation Request',
        help_text='Translation Request which this Activity is related to'
    )
    activity_type = models.CharField(
        'Activity Type',
        max_length=3,
        choices=choices.ACTIVITY_CHOICES,
        help_text='Type of the activity from the list of pre-selected ones'
    )
    responsible = models.ForeignKey(
        User,
        on_delete=models.RESTRICT,
        related_name='activities',
        verbose_name='Responsible',
        help_text='Registered user responsible for performing the activity'
    )
    expected_duration = models.DurationField(
        "Expected Duration",
        blank=True,
        null=True,
        help_text='Expected duration for the activity. Default is 1 hour'
    )
    actual_duration = models.DurationField(
        "Actual Duration",
        blank=True,
        null=True,
        help_text='Actual duration of the activity.'
    )
    # TODO: Re-write this to Foreign Key when the model is created.
    outsource = models.BooleanField(
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Activity'
        verbose_name_plural = 'Activities'

    def __str__(self):
        return (f'{self.get_activity_type_display()} '
                f'of {self.translation_request.email_subject[:15]} '
                f'requested by {self.translation_request.requester.name}')
