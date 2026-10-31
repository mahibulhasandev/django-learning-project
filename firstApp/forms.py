from django import forms
from .models import multipleVarient, Store

class MultipleItemForm(forms.Form):
    item_varity = forms.ModelChoiceField(queryset=multipleVarient.objects.all(), label="Select item variety")

    # item_varity = forms.CharField()