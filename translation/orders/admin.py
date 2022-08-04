from django.contrib import admin

from .models import (Activity, Company, Document, Outsource, Requester,
                     TranslationRequest)


@admin.register(Requester)
class RequesterAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'email',
    )
    search_fields = ('name',)
    empty_value_display = '-empty-'


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'code',
    )
    search_fields = ('name', 'code',)
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
        'type',
        'responsible',
        'expected_duration',
        'actual_duration',
        'outsource',
    )
    empty_value_display = '-empty-'


@admin.register(Outsource)
class OutsourceAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'agency',
        'activity',
        'status',
        'deadline',
        'standard_pages',
        'dtp_cat_1',
        'dtp_cat_2',
        'dtp_cat_3',
        'dtp_cat_4',
        'cost',
    )
    list_filter = ('agency', 'deadline',)
    empty_value_display = '-empty-'


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'number',
        'source_language',
        'translated_language',
        'source_title',
        'translated_title',
        'revision',
        'file_name',
        'file_type',
        'number_of_pages',
        'company',
    )
    search_fields = ('number', 'source_title', 'translated_title', 'file_name')
    list_filter = ('source_language', 'translated_language',
                   'file_type', 'company')
    empty_value_display = '-empty-'
