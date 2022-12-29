
from django import forms

class ColorPickerForm(forms.Form):
    red_amount = forms.IntegerField(
        min_value=0,
        max_value=255,
        required=True,
        label='RedValue'
    )
    green_amount = forms.IntegerField(
        min_value=0,
        max_value=255,
        required=True,
        label='GreenValue'
    )
    blue_amount = forms.IntegerField(
        min_value=0,
        max_value=255,
        required=True,
        label='BlueValue'
    )