from django import forms
from .models import ShippingMethod, ShippingCost


class ShippingMethodForm(forms.ModelForm):

    class Meta:
        model = ShippingMethod
        fields = ['name', 'description', 'active',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class ShippingCostForm(forms.ModelForm):

    class Meta:
        model = ShippingCost
        fields = ['country','weight_from', 'weight_to', 'cost', 'method',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'