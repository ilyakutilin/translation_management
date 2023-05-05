from django import forms

from . import models


class RequesterForm(forms.ModelForm):
    class Meta:
        model = models.Requester
        fields = ("first_name", "middle_name", "last_name", "email")
