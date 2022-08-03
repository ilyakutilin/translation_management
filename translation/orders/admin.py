from django.contrib import admin

from .models import Activity, Requester, TranslationRequest


@admin.register(Requester)
class RequesterAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'email',
    )
    search_fields = ('name',)
    empty_value_display = '-empty-'


@admin.register(TranslationRequest)
class TranslationRequestAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'requester',
        'received',
        'email_subject',
        'tn_no',
        'requested_date',
        'strict_deadline',
        'comments',
        'current_stage',
        'submitted',
        'submitter',
        'status',
    )
    search_fields = ('email_subject', 'comments')
    list_filter = ('received', 'requested_date', 'submitted')
    empty_value_display = '-empty-'


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'translation_request',
        'activity_type',
        'responsible',
        'expected_duration',
        'actual_duration',
        'outsource',
    )
    empty_value_display = '-empty-'
