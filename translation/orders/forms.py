from django import forms

from . import models


class RequesterAddForm(forms.ModelForm):
    class Meta:
        model = models.Requester
        fields = ("first_name", "middle_name", "last_name", "email")


class RequesterEditForm(RequesterAddForm):
    class Meta(RequesterAddForm.Meta):
        fields = RequesterAddForm.Meta.fields + ("is_active",)
