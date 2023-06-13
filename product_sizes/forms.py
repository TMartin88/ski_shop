from django import forms
from .models import ProductSize


class ProductSizeEditForm(forms.ModelForm):
    class Meta:
        model = ProductSize
        fields = ['size']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class ProductSizeAddForm(forms.ModelForm):
    class Meta:
        model = ProductSize
        fields = ['product', 'size', 'category']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
