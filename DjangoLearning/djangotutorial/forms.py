from django import forms
from .models import DjangoVariety


class DjangoVarietyForm(forms.Form):
    django_variety = forms.ModelChoiceField(queryset=DjangoVariety.objects.all(), label='Select Django Variety')
